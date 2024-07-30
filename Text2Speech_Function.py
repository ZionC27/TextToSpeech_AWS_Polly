import boto3
import json
import os
import base64

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Initialize Polly client
    polly = boto3.client('polly')

    try:
        # Get text and language from API Gateway event (from website)
        #body = json.loads(event['body'])
        text = str(event['text'])
        language = str(event['language'])

        # Validate input
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing "text" parameter in request body'})
            }


        if language == "en-US":
            VoiceIdName = "Joanna"
        elif language == "zh-CN":
            VoiceIdName = "Zhiyu"
        elif language == "ja-JP":
            VoiceIdName = "Mizuki"

        # Perform Text-to-Speech conversion
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat='mp3',
            LanguageCode=language,
            VoiceId=VoiceIdName
        )

        # Read audio stream into memory
        if 'AudioStream' in response:
            audio_stream = response['AudioStream'].read()
            
            # Encode audio bytes to base64 for transmission
            audio_base64 = base64.b64encode(audio_stream).decode('utf-8')
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'Polly service did not return an audio stream'})
            }

        # Return audio data to website
        return {
            'statusCode': 200,
            'body': json.dumps({'audio_data': audio_base64})
        }

    except Exception as e:
        logger.error(f"Error: {str(e)}")  # Log the error for debugging
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'An error occurred during text-to-speech conversion'})
        }