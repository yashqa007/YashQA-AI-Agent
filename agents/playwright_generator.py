from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_playwright_script(requirement):
    prompt = f"""
You are a QA Automation Engineer using Playwright with TypeScript.

Generate a complete Playwright test script for the following requirement:

Requirement:
{requirement}

Rules:
- Use TypeScript Playwright syntax
- Use @playwright/test
- Include test.describe and test()
- Use proper locators
- Add assertions using expect
- Keep code clean and production-ready
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content