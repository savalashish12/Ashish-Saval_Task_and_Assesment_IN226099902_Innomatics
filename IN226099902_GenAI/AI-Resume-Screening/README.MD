# 🚀 AI Resume Screening System (LangChain + LangSmith)

## 📌 Overview
This project is an AI-powered Resume Screening System that evaluates candidates based on a given Job Description using LLM pipelines.

It simulates a real-world recruiter workflow by performing:
- Skill extraction
- Resume vs Job Description matching
- Candidate scoring (0–100)
- Explainable evaluation

---

## 🎯 Objective
To build an intelligent system that:
- Automates resume screening
- Provides transparent scoring
- Uses LangChain pipelines
- Enables debugging using LangSmith tracing

---

## ⚙️ Features
- 📄 Resume parsing (PDF)
- 📌 Job Description skill extraction
- 🔍 Skill matching logic
- 📊 Score calculation (0–100)
- 🧠 Explainable AI output
- 🔗 LangSmith tracing for monitoring
- 📁 Automatic output file generation

---

## 🧠 Pipeline Architecture
Resume → Extract → JD Extract → Match → Score → Explain


---

## 🛠️ Tech Stack
- Python
- LangChain (LCEL + PromptTemplate)
- LangSmith (Tracing)
- Groq API (LLaMA 3)
- PyPDF

---

## 📂 Project Structure

AI-Resume-Screening/
│── prompts/
│── chains/
│── utils/
│── data/
│── Outputs/
│── main.py
│── requirements.txt
│── README.md


---

## 📊 Sample Output

**Candidate: Ashish Saval**
- Score: 70+
- Matched Skills: 14/20
- Missing Skills: GitHub, HuggingFace, LangSmith
- Experience: 4.5 years

---

## 🧪 Test Cases

| Candidate Type | Description        | Expected Score |
|---------------|------------------|---------------|
| Strong        | AI/ML background | High (70–90)  |
| Average       | Basic skills     | Medium (40–70)|
| Weak          | Non-DS profile   | Low (<30)     |

---
## 🧠 Explainability Logic
The system provides reasoning based on:
- Matched skills count
- Missing critical skills
- Candidate experience impact

---

## 🔐 Environment Variables

Create a `.env` file:


LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
GROQ_API_KEY=your_groq_key


---
---

## ▶️ How to Run

### 1. Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Run Project

python main.py


---

## 📁 Output Files

After execution, results are saved in:


Outputs/
Ashish Saval.txt
Nitin Satarkar.txt
Ram Kachare.txt


---

## 🧩 Key Learnings
- Building modular LLM pipelines using LangChain
- Designing explainable AI systems
- Debugging using LangSmith tracing
- Handling structured JSON outputs

---

## ⚠️ Important Notes
- No hardcoded outputs used
- No hallucinated assumptions
- Fully dynamic pipeline execution
- Supports multiple resumes

---

## 📌 Future Improvements
- Add UI (Streamlit / React)
- Improve scoring logic with weights
- Add database storage
- Integrate real recruiter workflow

---