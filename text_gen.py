import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def gpt_transform_reddit_post(content):
    paragraphs = ''.join(content['post_paragraphs'])

    prompt = (
        "Transform the following Reddit post into an engaging, click-bait, and conspiracy-themed narrative suitable for TikToks and Reels. "
        "Make the text highly entertaining, with a perspective that draws the audience in and keeps them hooked. Refer to popular short-form content styles "
        "found on TikTok and Reels for inspiration. The text should be compelling and formatted to be read by a text-to-speech algorithm.\n\n"
        f"Reddit Post:\n{paragraphs}"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant who transforms Reddit posts for social media entertainment."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion

# Example usage:
# content = {'post_paragraphs': ["Just saw a huge bird in my backyard. Never seen anything like it!"]}
# transformed_content = gpt_transform_reddit_post(content)
# print(transformed_content)
