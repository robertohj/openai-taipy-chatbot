from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(verbose=True,override=True)

# In the new SDK, the API Key is read automatically, no need to pass it
# (it actually causes an error if we pass the parameter)
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def chat_with_llm(messages, model = "gpt-4.1-nano"):
# Note that model's performance and accuracy may vary. Choose the model that best fits your use case.
# Models and pricing: https://openai.com/api/pricing/ and here https://platform.openai.com/docs/pricing
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_completion_tokens=50,
        temperature=0.7
    )
    return response.choices[0].message.content

