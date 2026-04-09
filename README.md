# co-napilot 🚀

AI-powered assistant for planning baby routines and daily activities.

---

## 🧠 Overview

**co-napilot** is a full-stack application designed to help users (especially parents) organize daily routines through AI-assisted planning.

The system uses a backend powered by Python and FastAPI, integrates AI models for intelligent suggestions, and provides a modern frontend interface using Next.js.

The core idea is to implement a simple **agent-based system** that:

* receives user input
* processes it using AI
* returns structured and useful plans

---

## 🏗️ Architecture

The project follows a **monorepo structure**:

```
co-napilot/
├── frontend/   # Next.js (React)
├── backend/    # FastAPI (Python)
├── tests/      # Playwright (E2E tests)
```

### Backend

* FastAPI for API development
* AI integration via external APIs
* Modular structure (routes, agent logic, database)

### Frontend

* Next.js (React)
* Component-based UI
* API communication layer

### Testing

* Playwright for end-to-end testing

---

## ⚙️ Tech Stack

* **Frontend:** Next.js (React)
* **Backend:** Python + FastAPI
* **Database:** SQLite (initially)
* **AI:** LLM APIs (e.g. OpenAI)
* **Testing:** Playwright

---

## 🤖 Core Concept: Agent Logic

The system is designed around a simple agent workflow:

1. User provides input
2. The system interprets intent
3. AI generates a structured plan
4. The result is returned and optionally stored

This allows the application to evolve into more complex multi-step agents.

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone <your-repo-url>
cd co-napilot
```

---

### 2. Backend setup

```
cd backend
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn openai python-dotenv
uvicorn main:app --reload
```

---

### 3. Frontend setup

```
cd frontend
npm install
npm run dev
```

---

## 🔐 Environment Variables

Create a `.env` file in the root:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🧪 Running Tests

```
npx playwright test
```

---

## 📌 Project Goals

* Build a real-world full-stack application
* Integrate AI into practical workflows
* Apply software engineering best practices
* Explore agent-based system design
* Ensure quality through testing

---

## 📄 License

MIT License