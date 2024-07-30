

*** fees may apply 

1. IAM Role for Lambda function ( Lambda_Polly_Role )
    - AmazonPollyReadOnlyAccess, AWSLambdaBasicExecutionRole
```JSON
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Principal": {
                "Service": [
                    "lambda.amazonaws.com"
                ]
            }
        }
    ]
}
```

2. Create the lambda function
   - Change default execution role -> Use an existing role -> Lambda_Polly_Role
