# 🤖 YashQA AI Agent

AI-powered QA Assistant that generates:

✅ Manual Test Cases  
✅ Playwright TypeScript Automation Scripts  

from natural language requirements using LLMs.

---

## 🚀 Features
- Generate structured manual test cases
- Generate Playwright TypeScript automation scripts
- Clean modular agent-based architecture
- Uses Groq LLM (LLaMA 3)

---

## 🛠️ Tech Stack
- Python
- Groq API (LLM)
- Playwright (for script generation)
- dotenv

---

## 📁 Project Structure
YashQA-AI-Agent/
│── agents/
│ ├── test_case_generator.py
│ ├── playwright_generator.py
│
|── output/
│── prompts/
│── utils/
│── main.py
│── .env
│── README.md
│── requirements.txt


---

## ⚙️ Setup

```bash
git clone https://github.com/yashqa007/YashQA-AI-Agent.git
cd YashQA-AI-Agent

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## 🔐 Environment Variables
Create .env file:

GROQ_API_KEY=your_api_key_here

## ▶️ Run
```bash
python main.py

##💡 Example
Input:

Login functionality with email and password

Output:
Manual Test Cases OR
Playwright TypeScript Script

##🚀 Upcoming Features
Web UI integration
FastAPI backend
Live deployment

# 👨‍💻 Author
Yash Rahate
QA Automation Engineer  
🔗 GitHub: https://github.com/yashqa007
🔗 Portfolio : https://yashqa007.github.io/Yash-QA-Portfolio/