from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

response = llm.invoke("Generate 3 test cases for login functionality")

print(response.content)