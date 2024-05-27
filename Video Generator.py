import boto3


def text_to_speech(text, output_file, voice_id="Joanna"):
    polly_client = boto3.Session(
        aws_access_key_id='YOUR_AWS_ACCESS_KEY_ID',
        aws_secret_access_key='YOUR_AWS_SECRET_ACCESS_KEY',
        region_name='us-west-2'
    ).client('polly')

    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id
    )

    with open(output_file, "wb") as out:
        out.write(response['AudioStream'].read())


# Example usage
if __name__ == "__main__":
    sample_text = "Hello, this is a sample text converted to speech using Amazon Polly."
    text_to_speech(sample_text, "output.mp3")
