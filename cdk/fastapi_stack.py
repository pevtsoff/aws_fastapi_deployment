from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_iam as iam
)
from constructs import Construct
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_ecs as ecs
import aws_cdk.aws_ecs_patterns as ecs_patterns


class FastAPIStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # (i) Create VPC
        self.vpc = ec2.Vpc(self, "MyVPC", max_azs=3)

        # (ii) Create Fargate Cluster
        self.ecs_cluster = ecs.Cluster(
            self,
            "MyECSCluster",
            vpc=self.vpc,
        )
        # createa dynamodb table
        self.table = dynamodb.Table(
            self,
            "MessagesTable",
            table_name="Messages",  # Explicit table name
            partition_key={"name": "id", "type": dynamodb.AttributeType.STRING},
            removal_policy=RemovalPolicy.DESTROY,
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST
        )

        # (iii) Define Docker image for the Service
        image = ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
            image=ecs.ContainerImage.from_asset(
                directory="../src",
            )
        )

        # (iv) Create Fargate Service and ALB
        self.ecs_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            "FastAPIService",
            cluster=self.ecs_cluster,
            cpu=256,
            memory_limit_mib=512,
            desired_count=2,
            task_image_options=image,
        )

        self.table.grant_read_write_data(self.ecs_service.task_definition.task_role)