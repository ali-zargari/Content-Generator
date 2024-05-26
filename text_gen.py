import os
from openai import OpenAI


client = OpenAI(
    # This is the default and can be omitted
    api_key="sk-proj-tvZmB1Skm7GJhqU3DVokT3BlbkFJUZiIFagE7hu0ugYFfvFj",
)
def gpt_summarize(content):


    paragraphs = ''.join(content['post_paragraphs'])

   # print(str_paragraphs)


    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant who summarizes posts. Give me the summary of the main post, and JUST that. nothing else. "},
            {"role": "user", "content": f"Please do it for the following content: {paragraphs}"}
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion

# print(gpt_summarize)

