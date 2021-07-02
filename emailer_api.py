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
        message = get_message(event)
        recipient_email = message["email_address"]
        recipient_name = message["first_name"]

        mailed_response = send_it(recipient_email, recipient_name)

        return {
            'statusCode': 200,
            'body': json.dumps("Email sent! Message ID: " + mailed_response['MessageId'])
        }
        
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(str(type(e).__name__) + ": " + str(e))
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
            'statusCode': 400,
            'body': json.dumps(e.response['Error']['Message'])
        }

def get_body(name):
    body = (f"Thank you {name} for your enquiry\r\n"
         "A member of our team will call you within the next few days."
        )
    return body

def get_message(event):
    # determine whether incoming data is from SNS or public API endpoint
    for k, v in event.items():
        if k == "Records": 
            try:
                message = json.loads(event['Records'][0]['Sns']['Message'])
            except Exception as e:
                raise e
        else:
            # data is not coming from SNS
            try:
                # convert string json to json object
                message = json.loads(event)
            except TypeError:
                # if data is not a string, assume it is already json
                message = event
            except Exception as e:
                raise e
    return message
    
    