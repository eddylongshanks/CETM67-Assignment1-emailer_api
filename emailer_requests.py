""" odip Requests
"""

import json
from requests import post, get

# oDip Endpoint
BASE_URL = "http://ec2-18-168-225-13.eu-west-2.compute.amazonaws.com"

# CREATE a new enquiry
data = {
    "first_name": "vs_oDip_API1",
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

response = get(BASE_URL)
print("GET Healthcheck... (/)")
print("Response: " + response.text)

response = get(BASE_URL + "/log")
print("GET Log... (/log)")
print("Response: " + response.text)

response = post(BASE_URL + "/send-enquiry", json = data)
print("POST New Enquiry... (/send-enquiry)")
print("Response: " + response.text)
