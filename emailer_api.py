import boto3
from botocore.exceptions import ClientError

# Required Variables
SENDER = "Newcastle Building Society <aws@holmescentral.co.uk>"
AWS_REGION = "eu-west-2"
SUBJECT = "Your Enquiry"
BODY_TEXT = ("Thank you for your enquiry\r\n"
             "A member of our team will call you within the next few days."
            )
CHARSET = "UTF-8"

mailer = boto3.client('ses', region_name=AWS_REGION)

def lambda_handler(event, context):
    mail = send_it("chris@holmescentral.co.uk")

def send_it(self, recipient):
    try:
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
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER        
        )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])