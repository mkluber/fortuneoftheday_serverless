import json
import boto3


dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('Fortunes')

def lambda_handler(event, context):
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json",
    }
    
    response = table.scan()
    body = response['Items']

    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': headers
    }
