import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Fortunes')

def handler(event, context):
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json",
    }
    
    response = table.scan()
    body = response['Items']

    return {
        'statusCode': status_code,
        'body': body,
        'headers': headers
    }
