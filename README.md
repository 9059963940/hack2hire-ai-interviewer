🚀 Hack2Hire: AI-Powered Interview Simulation Platform
🧠 Overview

Hack2Hire is an AI-powered mock interview simulation system that replicates real-world technical interviews.
It evaluates candidates based on their resume, job description alignment, answers, time management, and adaptability, and generates an objective Interview Readiness Score.

The system behaves like an AI Interviewer that thinks, adapts, evaluates, and decides in real-time.

🎯 Problem Statement

Traditional interview preparation systems suffer from:

Lack of realistic interview simulation
No structured evaluation system
No adaptive questioning based on performance
No time-aware scoring mechanism
No clear interview readiness indicator

This platform solves all the above using AI + state-based simulation.

⚙️ Core Features
🧾 Resume & JD Analysis
Extracts skills, experience, and project details from resume
Analyzes Job Description requirements
Computes skill match score

🤖 AI Interview Engine
Generates:
Technical questions
Behavioral questions
Scenario-based questions
Adapts difficulty dynamically (Easy → Medium → Hard)

⏱️ Time-Aware Evaluation
Fixed time per question
Penalizes delayed or incomplete responses

🧠 Adaptive Interview Logic
Increases difficulty for strong answers
Reduces difficulty for weak answers
Maintains interview state throughout session

📊 Smart Scoring System

Evaluates each response based on:

Accuracy
Clarity
Depth
Relevance
Time efficiency

🧾 Final Output
Interview Readiness Score (0–100)
Skill-wise breakdown
Strengths & weaknesses
Hiring recommendation

🏗️ System Architecture
Frontend (Next.js)
        ↓
Backend API (FastAPI)
        ↓
Resume Parser + JD Analyzer
        ↓
AI Question Generator
        ↓
Interview State Machine
        ↓
Answer Evaluation Engine
        ↓
Scoring & Readiness Module
        ↓
Final Report Generator

🧑‍💻 Tech Stack
Frontend
Next.js (React)
Tailwind CSS
Backend
Python
FastAPI
AI/ML
OpenAI API / Gemini API
NLP-based evaluation prompts
Libraries
PyPDF (Resume parsing)
Pandas / NumPy
Scikit-learn (optional scoring logic)

📂 Project Structure
Hack2Hire/
│
├── backend/
│   ├── main.py
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── scoring.py
│   └── state_manager.py
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── upload/
│   │   ├── interview/
│   │   └── result/
│
├── README.md
└── requirements.txt


🚀 How to Run Locally

1️⃣ Clone Repository
git clone https://github.com/your-username/hack2hire-ai-interviewer.git
cd hack2hire-ai-interviewer

2️⃣ Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
uvicorn main:app --reload

Backend runs at:

http://localhost:8000


3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

Frontend runs at:

http://localhost:3000

