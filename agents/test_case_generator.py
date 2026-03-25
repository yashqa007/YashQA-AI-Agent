from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_test_cases(requirement):
    prompt = f"""
You are a QA Engineer.

Generate detailed manual test cases for the following requirement:

Requirement:
{requirement}

Format:
- Test Case ID
- Title
- Preconditions
- Steps
- Expected Result
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content