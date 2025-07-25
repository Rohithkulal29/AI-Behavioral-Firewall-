# 🛡️ AI Behavioral Firewall

An intelligent, real-time system that **intercepts and filters potentially unsafe, toxic, or biased AI outputs** using Natural Language Processing (NLP) and Deep Learning techniques. Built using FastAPI, Detoxify, and spaCy.

---

## 🚀 Features

- ✅ Detects toxicity using the [Detoxify](https://github.com/unitaryai/detoxify) model
- ✅ Redacts sensitive PII (Personal Identifiable Information) like names, locations, organizations using spaCy
- ✅ Logs every intercepted AI output with a timestamp for auditing
- ✅ Provides a RESTful API with interactive Swagger UI via FastAPI `/docs`
- ✅ Scalable backend architecture for integration with AI/ML pipelines

---

## 📦 Tech Stack

- **Python 3.10**
- **FastAPI** – Web framework for backend API
- **Detoxify** – Toxicity detection using BERT-based model
- **spaCy** – NLP library for entity recognition and redaction
- **Uvicorn** – Lightning-fast ASGI server
- **Git & GitHub** – Version control and collaboration

---

## 🧠 How It Works

1. A client or user sends AI-generated output to the `/intercept/` endpoint.
2. The backend:
   - Evaluates the output for toxicity using Detoxify.
   - If the output is toxic, it redacts sensitive info (names, places, orgs, etc.).
   - Saves the original and filtered outputs to a log file (`logs/intercepts_log.json`).
3. The API returns the filtered (safe) output along with a detailed report.

---

## 📂 Project Structure

AI-Behavioral-Firewall-/
├── .gitignore # Git ignore rules
├── main.py # FastAPI app (API logic and routing)
├── firewall.py # Core functions: toxicity detection, redaction, logging
├── logs/ # Auto-created folder to store intercepted logs
├── venv310/ # Python virtual environment (excluded from Git)
├── README.md # Project overview and documentation
└── ui/ # (Coming soon) Simple UI for interaction
