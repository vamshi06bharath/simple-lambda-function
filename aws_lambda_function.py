import boto3
import zipfile

def create_lambda_zip():
    """Creates a zip file for the lambda function."""
    with zipfile.ZipFile('lambda_function.zip', 'w') as zipf:
        zipf.write('lambda_function.py')

# AWS Lambda function code
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from AWS Lambda!'
    }

# Create a zip package
create_lambda_zip()

# Set up AWS Lambda function using Boto3
client = boto3.client('lambda')

response = client.create_function(
    FunctionName='MyLambdaFunction',
    Runtime='python3.8',
    Role='arn:aws:iam::YOUR_AWS_ACCOUNT_ID:role/YOUR_LAMBDA_ROLE',
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': open('lambda_function.zip', 'rb').read()},
    Description='My first AWS Lambda function via Boto3',
    Timeout=15,
    MemorySize=128,
    Publish=True
)

print("Lambda function created successfully:", response)
