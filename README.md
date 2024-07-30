# Text to Speech using AWS Polly 

## This project utilizes 

## System flow chart 


*** fees may apply 
https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-LanguageCode doc 

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

2. Create the lambda function (Text2Speech_Function)
   - Runtime -> Python 3.12
   - Change default execution role -> Use an existing role -> Lambda_Polly_Role
   - Copy the provided code into the Code source and Deploy
   - Optional: Test -> Configure test event use the following code
``` JSON
{
  "text": "Hello, this is a test of the text-to-speech system.",
  "language": "ja-JP"  
}
```

3. Create API Gateway
   - API endpoint type -> Edge-optimized
   - Create method -> Lambda -> (Method type) POST -> Lambda arn choose (Text2Speech_Function)
   - Press / on left hand side Enable CORS -> (Access-Control-Allow-Methods) POST
   - Deploy API - *New stage* -> dev
   - Copy Invoke URL in a Notepad ***https://mlsjr84gw0.execute-api.us-east-2.amazonaws.com/dev
  
4. Create a Website (index.html)
   - Use a text editor like VS and create a HTML file name index.html and Copy the provided code
   - Replace Invoke URL in line 70 to your own URL !!! remember that the URL form API Gateway ends with /dev but you need to add a backslash at the end Like /dev/
```js
fetch("Invoke URL", requestOptions)
```
   - Using File Explorer right click on index.html and compress to ZIP file !!! Must be in zip file it cannot be in rar or other type 

5. Create an AWS amplify app
   - Create new app
   - Choose Deploy without git
   - Then drag the zip file or choose zip folder -> Save and deploy 
  
6. Test the website
   - Type a sentence that you want to synthesize
   - Choose a language
   - Press synthesize to hear!
