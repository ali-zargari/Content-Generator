import boto3

def synthesize_speech(ssml_text, output_file):
    # Initialize a session using Amazon Polly
    polly_client = boto3.Session(
        aws_access_key_id='AKIAVRUVVYWSLAMUSIN2',
        aws_secret_access_key='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',
        region_name='us-west-2'
    ).client('polly')

    # Request speech synthesis
    response = polly_client.synthesize_speech(
        VoiceId='Gregory',  # Change this to a neural voice
        Engine='generative',  # Use neural engine for generative voice
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
        In April 1981, <break time="200ms"/> three members of the 
        <phoneme alphabet="ipa" ph="ʃɑːrp">Sharp</phoneme> family 
        and a family friend were <break time="200ms"/> <phoneme alphabet="ipa" ph="ˈbruːtəli">brutally</phoneme> 
        <phoneme alphabet="ipa" ph="ˈmɜːrdərd">murdered</phoneme> in a 
        <phoneme alphabet="ipa" ph="ˈkæbɪn">cabin</phoneme> at the 
        <phoneme alphabet="ipa" ph="ˈkɛdi">Keddie</phoneme> Resort in northern California. 
        <break time="500ms"/>
    </p>

    <p>
        The crime scene was horrifically <phoneme alphabet="ipa" ph="ˈvaɪələnt">violent</phoneme>, 
        with the <phoneme alphabet="ipa" ph="ˈvɪktɪmz">victims</phoneme> 
        <phoneme alphabet="ipa" ph="baʊnd">bound</phoneme>, 
        <phoneme alphabet="ipa" ph="ˈblʌʤənd">bludgeoned</phoneme>, and 
        <phoneme alphabet="ipa" ph="stæbd">stabbed</phoneme>. 
        <s>Despite initial suspects and ongoing investigations, the case went cold for many years.</s> 
        <break time="700ms"/>
    </p>

    <p>
        Recent re-examinations of the evidence and new leads have kept the case in the public eye, 
        but the murders remain <phoneme alphabet="ipa" ph="ʌnˈsɑːlvd">unsolved</phoneme>, 
        leaving a community <phoneme alphabet="ipa" ph="ˈhɔːntɪd">haunted</phoneme> by the brutal crime.
        <break time="500ms"/>
    </p>

    <p>
        <amazon:effect name="drc">
            This tragic event has deeply affected the residents, with the chilling memory still lingering.
        </amazon:effect>
    </p>
</speak>

    """

    output_file = 'output.mp3'
    synthesize_speech(ssml_text, output_file)
    print(f"Speech synthesized and saved to {output_file}")

