import json
import boto3
from botocore.exceptions import ClientError

# Required Variables
SENDER = "Newcastle Building Society <aws@holmescentral.co.uk>"
AWS_REGION = "eu-west-2"
SUBJECT = "Your Enquiry"
CHARSET = "UTF-8"

mailer = boto3.client('ses', region_name=AWS_REGION)

def lambda_handler(event, context):
    try:
        print(str(event))
        recipient_email = get_value(event, "email_address")
        print(recipient_email)
        
        recipient_name = get_value(event, "first_name")
        print(recipient_name)
        
        mailed_response = send_it(recipient_email, recipient_name)
        print(str(mailed_response))
        
        return {
            'statusCode': 200,
            'body': json.dumps("Email sent! Message ID: " + mailed_response['MessageId'])
        }
        
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': "1 " + json.dumps(str(e))
        }

def send_it(recipient, name):
    try:
        body_text = get_body(name)
        
        response = mailer.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER        
        )
        
        return response

    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps(e.response['Error']['Message'])
        }
    
def get_value(event, key):
    try:
        message = json.loads(event['Records'][0]['Sns']['Message'])
        value = message[key]
        return value
        
    except Exception as e:
        raise e

def get_body(name):
    body = (f"Thank you {name} for your enquiry\r\n"
         "A member of our team will call you within the next few days."
        )
    
    return body
    