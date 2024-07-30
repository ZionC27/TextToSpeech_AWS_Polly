# Text-to-Speech with AWS Polly

This project leverages AWS services to create a serverless text-to-speech application. Users can input text into a web interface, which is then sent to an AWS Lambda function via API Gateway. The Lambda function utilizes Amazon Polly, a service that converts text into lifelike speech, to generate an audio file of the input text. The audio is then played back to the user, allowing them to hear the synthesized speech.

By completing this project, you'll learn how to:
1. Set up and manage AWS services, including AWS Amplify for web hosting, API Gateway for communication, Lambda for processing data, and Polly for text-to-speech conversion.
2. Implement a serverless architecture for a real-world application.
3. Integrate these services to provide a seamless user experience from text input to speech output.

**Note: Fees may apply when using AWS services. It is recommended to delete all unused services after completing the project to avoid unnecessary charges.**

## System Flow Chart
![System Flow Chart](https://github.com/ZionC27/TextToSpeech_AWS_Polly/blob/main/FlowChartPolly.png)

## Setup Guide

### 1. IAM Role for Lambda Function (`Lambda_Polly_Role`)
Create an IAM role with the following permissions:
- **AmazonPollyReadOnlyAccess**
- **AWSLambdaBasicExecutionRole**


### 2. Create the Lambda Function (`Text2Speech_Function`)
- **Runtime**: Python 3.12
- **Execution Role**: Use an existing role (`Lambda_Polly_Role`)
- **Code**: Deploy the provided code in the Code source section.

**Optional**: To test the function, configure a test event using the following JSON:
```JSON
{
  "text": "Hello, this is a test of the text-to-speech system.",
  "language": "ja-JP"
}
```

### 3. Create API Gateway
- **API Endpoint Type**: Edge-optimized
- **Method**: POST
  - **Integration Type**: Lambda Function
  - **Lambda Function**: `Text2Speech_Function`
- **CORS**: Enable CORS on the root resource `/`
  - **Access-Control-Allow-Methods**: POST
- **Deployment**: Deploy the API to a new stage named `dev`
- **Invoke URL**: Copy the Invoke URL for later use

### 4. Create a Website (`index.html`)
- Use a text editor (e.g., VS Code) to create an `index.html` file.
- Insert the provided HTML code.
- Replace the placeholder in line 70 with your API Gateway Invoke URL, ensuring it ends with a backslash (`/dev/`):
  ```js
  fetch("Invoke URL", requestOptions)
  ```
- Compress the `index.html` file into a ZIP archive (it must be a `.zip` file, not `.rar` or another format).

### 5. Create an AWS Amplify App
- **Create New App**: Choose "Deploy without Git."
- **Upload ZIP File**: Drag and drop the ZIP file containing `index.html`, then save and deploy.
- **Access**: Click "Visit deployed URL" or use the provided Domain URL to access your app.

### 6. Test the Website
- Enter a sentence to synthesize.
- Select a language.
- Click "Synthesize" to hear the generated speech.

## Additional Information
For more details on the `SynthesizeSpeech` API, refer to the [Polly SynthesizeSpeech documentation](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html#polly-SynthesizeSpeech-request-LanguageCode).
