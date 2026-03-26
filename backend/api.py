from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from agents.test_case_generator import generate_test_cases
from agents.playwright_generator import generate_playwright_script

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    requirement: str
    type: str  # manual or automation


@app.get("/")
def home():
    return {"message": "AI QA Agent API is running"}


@app.post("/generate")
def generate(data: RequestData):
    if data.type == "manual":
        result = generate_test_cases(data.requirement)

    elif data.type == "automation":
        result = generate_playwright_script(data.requirement)

    else:
        return {"error": "Invalid type"}

    return {"result": result}

@app.options("/{full_path:path}")
def preflight_handler():
    return {"message": "OK"}