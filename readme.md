## AWS Lambda Emailer API using AWS SES

Accepts a JSON object and determines the source between and external endpoint submission and an SNS message
Returns a 400 if the following data is not contained within the request:

```python
{
	"first_name": "[first name]",
	"email_address": "[email address]"
}
```