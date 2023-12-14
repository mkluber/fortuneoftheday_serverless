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

    fortune_key = event['updatefortune']
    origin_key = event['updateorigin']
    author = event['updateattribute1']
    color = event['updateattribute2']
    response = table.update_item(
        Key={
            'FortuneName': fortune_key,
            'FortuneOrigin': origin_key
        },
        AttributeUpdates={
            'FortuneAuthor': {
                'Value'  : author,
                'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
            },
            'FortuneColor': {
                'Value'  : color,
                'Action' : 'PUT' # available options -> DELETE(delete), PUT(set), ADD(increment)
            }
        }
    )

    return {
        'statusCode': status_code,
        'body': json.dumps(body),
        'headers': headers,
        'event': json.dumps(event)
    }

