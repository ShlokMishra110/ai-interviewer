# 🎤 AI Interviewer (Local LLM)

An AI-powered interview simulator that conducts **mock interviews**, evaluates answers, and provides **structured feedback with scoring** — built using **Streamlit** and **Ollama (local LLM)**.

> 🚀 Fully local AI system — no API costs, no data sharing

---

## ✨ Features

* 🎯 **Role-Based Questions**
  Generate interview questions tailored to specific job roles

* 📊 **Answer Evaluation**
  AI scores responses (0–10) based on quality, clarity, and correctness

* 📖 **Detailed Feedback**
  Highlights strengths and weaknesses

* 🚀 **Improvement Suggestions**
  Actionable tips to improve answers

* 🔁 **Multi-Round Interviews**
  Simulates real interview experience with multiple questions

* 🎚 **Difficulty Levels**
  Easy / Medium / Hard question generation

* ⏱️ **Answer Timing**
  Tracks how long you take to respond

* 🔒 **Runs Locally**
  Powered by Ollama — no external APIs required

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Ollama (Local LLM)**
* **Requests**

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash id="c7b2p9"
git clone https://github.com/YOUR_USERNAME/ai-interviewer.git
cd ai-interviewer
```

### 2️⃣ Install Dependencies

```bash id="p25n4p"
pip install -r requirements.txt
```

### 3️⃣ Start Ollama

```bash id="9ws6ss"
ollama serve
```

### 4️⃣ Run the Application

```bash id="s0eky1"
streamlit run app.py
```

---

## 🧪 Example Use Case

### 🔹 Role Input

```text id="y7m3q9"
Backend Developer
```

### 🔹 AI Generated Question

```text id="z8k2pj"
Explain REST API principles and why statelessness is important.
```

### 🔹 AI Evaluation Output

```text id="9l0x8p"
Score: 7/10

Feedback:
Good understanding of APIs, but missing details about statelessness and HTTP methods.

Improvement:
Include examples of HTTP verbs (GET, POST) and explain scalability benefits.
```

---

## 🖥️ Screenshots

*Add screenshots here after running the app (recommended for better presentation)*

---

## 🔥 Future Improvements

* 🎤 Voice-based interview (speech input/output)
* 🧠 AI follow-up questions (dynamic interviews)
* 📊 Final score aggregation & performance report
* 📂 Interview history tracking
* 🤖 Personality & communication analysis

---

## 💡 Inspiration

Inspired by modern AI-driven hiring platforms like:

* HireVue
* LinkedIn

---

## 📌 Project Highlights

* Built a **multi-step AI system pipeline**
* Implemented **LLM-based evaluation (LLM-as-a-Judge)**
* Designed **stateful user interactions using Streamlit**
* Created a **real-world AI product simulation**

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork and improve it
* 💡 Suggest new features

---

## 📬 Contact

Open to collaboration and feedback!
