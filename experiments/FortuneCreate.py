import json
import boto3


dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('Fortunes')

def lambda_handler(event, context):
    print(json.dumps(event))
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json",
    }

    body_content = json.loads(event['body'])
    fortune_key = body_content['addfortune']
    origin_key = body_content['addorigin']
    response = table.put_item(
        Key={
            'FortuneName': fortune_key,
            'FortuneOrigin': origin_key
        }
    )

    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'response': json.dumps(response),
        'headers': headers,
        'event': json.dumps(event)
    }

