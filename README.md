## Fastapi Deployment with DynamoDB and CDK
This is a template for FastAPI App deployment into AWS with DynamoDB


## Testing
```angular2html
curl "http://FastAP-FastA-SPztTrePt9Uk-1781643704.eu-west-2.elb.amazonaws.com/messages" -H "Content-Type: application/json"  -d '{"id":"1", "message": "hello world"}'
{"id":"1","message":"hello world"}

curl "http://FastAP-FastA-SPztTrePt9Uk-1781643704.eu-west-2.elb.amazonaws.com/messages/1"
{"message":"hello world"}
```