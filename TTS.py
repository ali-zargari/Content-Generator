import os

import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

def synthesize_speech(ssml_text, output_file):
    # Initialize a session using Amazon Polly
    polly_client = boto3.Session(
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name=AWS_REGION
    ).client('polly')

    # Request speech synthesis
    response = polly_client.synthesize_speech(
        VoiceId='Ruth',  # Change this to a neural voice
        Engine='neural',  # Use neural engine for generative voice
        OutputFormat='mp3',
        TextType='ssml',
        Text=ssml_text
    )

    # Save the audio stream returned by Amazon Polly
    with open(output_file, 'wb') as file:
        file.write(response['AudioStream'].read())


if __name__ == '__main__':
    ssml_text = """
<speak>
    <p>
        Uncover the SHOCKING truth behind AI text generation! <break time="500ms"/>
    </p>
    
    <p>
        SECRET AI CONSPIRACY REVEALED: How FREE users accessed custom GPTs reserved for PLUS+ accounts! <break time="500ms"/>
    </p>
    
    <p>
        Have you ever wondered how some got LIMITED access to GPT4O without PLUS+ perks? Could it be a glitch... or something SINISTER? <break time="700ms"/>
    </p>
    
    <p>
        DIVE into the subreddit for AI tech and UNRAVEL the mystery of FREE users INTRUDING into PLUS+ territory! <break time="700ms"/>
    </p>
    
    <p>
        Explore the DARK side of AI text generation and DISCOVER how the UNEXPECTED became reality! <break time="500ms"/>
    </p>
    
    <p>
        DON'T miss this mind-blowing TWIST in the world of AI! #AIconspiracy #GPT4O #SecretRevealed
    </p>
</speak>

    """

    output_file = 'output.mp3'
    synthesize_speech(ssml_text, output_file)
    print(f"Speech synthesized and saved to {output_file}")

