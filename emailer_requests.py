""" Emailer Requests
"""

import json
from requests import post, get

# Emailer Endpoint
BASE_URL = "https://a4j7i493vh.execute-api.eu-west-2.amazonaws.com/dev"

# CREATE a new enquiry
data = {
    "first_name": "vs_Emailer_API1",
    "last_name": "Smith",
    "building": "11",
    "street": "Indigo Avenue",
    "town": "Newcastle",
    "county": "Tyne and Wear",
    "postcode": "NE2 3JM",
    "telephone_number": "07777777778",
    "email_address": "test@holmescentral.co.uk",
    "preferred_time_to_contact": "S",
    "annual_income": "30000",
    "loan_amount": "10000",
    "property_value": "100000",
    "mortgage_type": "RM",
    "ltv_value": "5"
}

response = post(BASE_URL + "/send", json = data)
print("POST New Enquiry... (/send)")
print("Response: " + response.text)
