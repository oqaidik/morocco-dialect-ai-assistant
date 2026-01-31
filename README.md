🇲🇦 Morocco Voice MVP — Multilingual Speech AI System (EN ↔ Darija)

Morocco Voice is a production-ready multilingual speech AI pipeline that enables bidirectional voice and text communication between English and Moroccan Darija, a low-resource dialect.

🔗 Live Demo (Mobile-friendly): https://mvp-morocco-voice.onrender.com/demo

📘 API Documentation (Swagger): https://mvp-morocco-voice.onrender.com/docs

🚀 What This Project Demonstrates

This MVP is designed as a real-world AI system, not just a demo.

It showcases:

End-to-end Speech AI pipelines

Integration of STT → LLM → TTS

Clean, stateless FastAPI microservice

Deployment-ready architecture for mobile apps

AI-assisted communication for a low-resource language (Darija)

🎯 Core Capabilities 🔊 English → Darija (“Speak for Me”)

Input

English text

Output

Darija text (Arabic script)

Darija phonetic transcription

Darija speech audio (TTS)

Context-aware alternative replies

Use case

Helping non-Darija speakers communicate naturally in Morocco (travel, services, daily life).

🎧 Darija → English (“Translate”)

Input

Darija speech audio

Output

English transcription

English translation

English speech audio (TTS)

Use case

Voice-based translation for real-life conversations.

🧠 AI System Architecture Client (Mobile / Web Demo) | v FastAPI Backend (Stateless) ├── Speech-to-Text (STT) │ └── Audio normalization & transcription ├── Large Language Model (LLM) │ └── Translation, reasoning, Darija generation ├── Text-to-Speech (TTS) │ └── Audio synthesis (Darija / English) └── JSON API (Mobile-ready)

Design choices

Modular services (STT / LLM / TTS decoupled)

JSON-first LLM prompting (robust parsing)

Explicit latency tracking

Graceful error handling for STT & TTS failures

🛠 Tech Stack

Backend

Python, FastAPI

Async request handling

Speech & Language

Speech-to-Text: Whisper-compatible STT

LLM: OpenAI (structured JSON prompting)

Text-to-Speech: Google Cloud Text-to-Speech

Deployment

Render (production)

Environment-based configuration

Frontend

Mobile-first HTML demo (no framework, API-driven)

📦 Project Structure mvp-morocco-voice/ ├── app/ │ ├── main.py # API entry point │ ├── llm.py # LLM orchestration │ ├── stt.py # Speech-to-Text logic │ ├── tts.py # Text-to-Speech logic │ ├── prompts.py # Structured LLM prompts │ ├── schemas.py # Pydantic models │ └── utils.py ├── static/ │ └── tts/ # Generated audio files ├── ui/ │ └── demo.html # Mobile-friendly demo ├── requirements.txt ├── .env.example └── README.md

⚙️ Environment Configuration

Create a .env file (never committed):

LLM
OPENAI_API_KEY=your_openai_key LLM_MODEL=gpt-4o-mini

Speech-to-Text
STT_MODEL=whisper-1

Google TTS
GOOGLE_APPLICATION_CREDENTIALS_JSON={json_string_or_path} GOOGLE_TTS_VOICE_EN=en-US-Wavenet-D GOOGLE_TTS_VOICE_AR=ar-XA-Wavenet-D

App
BASE_URL=http://localhost:8000

▶️ Run Locally pip install -r requirements.txt uvicorn app.main:app --reload --port 8000

API Docs: http://localhost:8000/docs

Demo: http://localhost:8000/demo

🧪 API Overview POST /talk

Unified multimodal endpoint.

Modes

speak_for_me

translate

explain

Supports:

Text input

Audio input

JSON responses with audio URLs

📈 Roadmap (Engineering-Focused)

✔ End-to-end speech AI pipeline

✔ Production deployment

✔ Mobile-friendly demo

🔄 Improved Darija pronunciation & prosody

🔄 Caching & latency optimization

🔄 Optional fine-tuning / prompt optimization

🔄 Authentication & usage tracking

🔄 React Native mobile client

🎯 Why This Project Matters

This project demonstrates:

Applied Machine Learning engineering

AI system integration, not just model usage

Handling of low-resource languages

Production-oriented thinking (deployment, API design, UX)

👤 Author

Dr. Khalid Oqaidi PhD in Computer Science & Artificial Intelligence AI Researcher · ML Engineer · Educator 📍 Germany / Morocco
