from boto3.dynamodb.conditions import Key
from boto3.dynamodb.types import TypeDeserializer
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('http-crud-tutorial-items')

def lambda_handler(event, context):
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json",
    }

    try:
        route_key = event['routeKey']
        path_parameters = event['pathParameters']
        query_string_parameters = event['queryStringParameters']
        http_method = event['httpMethod']
        request_context = event['requestContext']
        body = event['body']

        if http_method == 'DELETE':
            table.delete_item(
                Key={
                    'id': path_parameters['id']
                }
            )
            body = f"Deleted item {path_parameters['id']}"
        elif http_method == 'GET':
            if path_parameters and 'id' in path_parameters:
                response = table.get_item(
                    Key={
                        'id': path_parameters['id']
                    }
                )
                body = response['Item']
            else:
                response = table.scan()
                body = response['Items']
        elif http_method == 'PUT':
            item = TypeDeserializer().deserialize(body)
            table.put_item(Item=item)
            body = f"Put item {item['id']}"
        else:
            raise Exception(f"Unsupported route: {route_key}")
    except Exception as e:
        status_code = 400
        body = str(e)
    finally:
        body = json.dumps(body)

    return {
        'statusCode': status_code,
        'body': body,
        'headers': headers
    }
