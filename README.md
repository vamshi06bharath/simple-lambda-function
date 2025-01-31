# AWS Lambda Setup Guide

## Prerequisites
Before setting up the AWS Lambda function, ensure you have the following installed:
- **Python 3.8 or later**: [Download Python](https://www.python.org/downloads/)
- **AWS CLI**: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- **Boto3 (AWS SDK for Python)**: Install it using `pip install boto3`
- **IAM Role with Lambda Permissions**: Create an IAM role with `AWSLambdaBasicExecutionRole`

## Steps to Create and Deploy AWS Lambda
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/aws-lambda-setup.git
   cd aws-lambda-setup
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Modify the **aws_lambda_function.py** file:
   - Replace `YOUR_AWS_ACCOUNT_ID` with your AWS account ID.
   - Replace `YOUR_LAMBDA_ROLE` with the IAM role ARN that has Lambda execution permissions.

4. Run the script to create and deploy the Lambda function:
   ```sh
   python aws_lambda_function.py
   ```

5. Verify the Lambda function in AWS Console:
   - Navigate to **AWS Console > Lambda**.
   - Look for `MyLambdaFunction` and check its details.

## Steps to Use the Lambda Function
1. Invoke the function from AWS CLI:
   ```sh
   aws lambda invoke --function-name MyLambdaFunction response.json
   ```
2. Check `response.json` for the Lambda function response.

## Cleanup (Optional)
To delete the Lambda function:
```sh
aws lambda delete-function --function-name MyLambdaFunction
```

## Notes
- Ensure your AWS CLI is configured using `aws configure`.
- You may need to update the AWS Lambda execution role with additional permissions depending on your use case.

Happy coding! 🚀
