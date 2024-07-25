## Fastapi Deployment with DynamoDB using CDK
This is a template for FastAPI App deployment into AWS with DynamoDB


## Run
```angular2html
cd cdk
cdk deploy

aftger it has been deployed, you can remove it

cdk destroy
```
## Python dependencies

aws_requirements.txt are only for deployment via cdk
src/requirements.txt  is fastapi dependencies

## Testing
```angular2html
curl "http://FastAP-FastA-SPztTrePt9Uk-1781643704.eu-west-2.elb.amazonaws.com/messages" -H "Content-Type: application/json"  -d '{"id":"1", "message": "hello world"}'
{"id":"1","message":"hello world"}

curl "http://FastAP-FastA-SPztTrePt9Uk-1781643704.eu-west-2.elb.amazonaws.com/messages/1"
{"message":"hello world"}
```