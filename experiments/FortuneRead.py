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

    query_string_parameters = event['queryStringParameters']
    fortune_key = query_string_parameters['readfortune']
    origin_key = query_string_parameters['readorigin']
    response = table.get_item(
        Key={
            'FortuneName': fortune_key,
            'FortuneOrigin': origin_key
        }
    )
    body = response['Item']

    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': headers
    }

