from google.cloud import texttospeech
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Ensure the GOOGLE_APPLICATION_CREDENTIALS environment variable is set
credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if not credentials_path:
    raise ValueError("GOOGLE_APPLICATION_CREDENTIALS environment variable not set.")

# Now you can use the Google Cloud Text-to-Speech client

def synthesize_speech(ssml_text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", name="en-US-Wavenet-D")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to file {output_file}")

if __name__ == "__main__":
    ssml_text = """
    <speak>
        <p>
            <emphasis level="strong">Uncover the shocking truth</emphasis> behind AI text generation! <break time="500ms"/>
        </p>
        <p>
            <prosody pitch="+500%">Secret AI conspiracy revealed:</prosody> How <emphasis level="moderate">free users</emphasis> accessed custom GPTs reserved for PLUS+ accounts! <break time="500ms"/>
        </p>
        <p>
            <prosody pitch="+100%">Have you ever wondered how some got limited access to GPT4O without PLUS+ perks?</prosody> <break time="500ms"/> Could it be a glitch... or something sinister? <break time="700ms"/>
        </p>
        <p>
            <emphasis level="strong">Dive</emphasis> into the subreddit for AI tech and <emphasis level="strong">unravel</emphasis> the mystery of free users intruding into PLUS+ territory! <break time="700ms"/>
        </p>
        <p>
            <prosody rate="slow">Explore the dark side of AI text generation and discover how the unexpected became reality!</prosody> <break time="500ms"/>
        </p>
        <p>
            Don't miss this mind-blowing twist in the world of AI! <break time="500ms"/> <emphasis level="strong">#AIconspiracy #GPT4O #SecretRevealed</emphasis>
        </p>
    </speak>
    """

    output_file = "output.mp3"
    synthesize_speech(ssml_text, output_file)
