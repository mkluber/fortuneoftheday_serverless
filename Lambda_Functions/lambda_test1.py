import boto3
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    # Set up the client for DynamoDB and SES
    dynamodb = boto3.client('dynamodb')
    ses = boto3.client('ses')

    # Get all the fortunes from the DynamoDB table
    response = dynamodb.scan(TableName='Fortunes')
    fortunes = response['Items']

    # Create the message body
    message_body = ''
    for fortune in fortunes:
        message_body += fortune['FortuneName']['S'] + ' ' + fortune['FortuneOrigin']['S'] + '\n'

    # Send the email
    response = ses.send_email(
        Source='YOUREMAILADDRESS',
        Destination={
            'ToAddresses': ['YOUREMAILADDRESS']
        },
        Message={
            'Subject': {
                'Data': 'Fortunes for ' + datetime.today().strftime('%Y-%m-%d')
            },
            'Body': {
                'Text': {
                    'Data': message_body
                }
            }
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Email sent successfully')
    }