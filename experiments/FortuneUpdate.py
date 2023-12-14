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

    body_content = event['body']
    fortune_key = body_content['updatefortune']
    origin_key = body_content['updateorigin']
    author = body_content['updateattribute1']
    color = body_content['updateattribute2']
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
        'response': json.dumps(response),
        'headers': headers,
        'event': json.dumps(event)
    }
