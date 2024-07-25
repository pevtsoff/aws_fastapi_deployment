import boto3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from botocore.exceptions import ClientError



app = FastAPI()
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Messages')


class Message(BaseModel):
    id: str
    message: str


@app.post("/messages")
async def create_message(message: Message):
    try:
        table.put_item(Item={'id': message.id, 'message': message.message})
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"id": message.id, "message": message.message}


@app.get("/messages/{message_id}")
async def get_message(message_id: str):
    try:
        response = table.get_item(Key={'id': message_id})
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    item = response.get('Item')
    if item is None:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"message": item['message']}


@app.get("/")
def get_root():
    return {"message": "FastAPI running in a Docker container"}