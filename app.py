import streamlit as st
import requests
from prompts import generate_question, evaluate_answer

st.set_page_config(page_title="AI Interviewer", layout="wide")
st.title("🎤 AI Interviewer (Local - Ollama)")

# ------------------------
# Session State
# ------------------------
if "question" not in st.session_state:
    st.session_state.question = ""

if "question_count" not in st.session_state:
    st.session_state.question_count = 0

if "max_questions" not in st.session_state:
    st.session_state.max_questions = 3

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"

if "question" not in st.session_state:
    st.session_state.question = ""

# ------------------------
# Input Role
# ------------------------
role = st.text_input("Enter Job Role (e.g., Python Developer)")

difficulty = st.selectbox(
    "Select Difficulty:",
    ["Easy", "Medium", "Hard"]
)

st.session_state.difficulty = difficulty
# ------------------------
# Ollama API
# ------------------------
def query_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": "llama3",  # or codellama
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json().get("response", "Error generating response")

# ------------------------
# Generate Question
# ------------------------
if st.button("Start Interview"):
    if role:
        st.session_state.question_count = 0
        st.session_state.question = ""

# ------------------------
# Show Question
# ------------------------
if st.session_state.question_count < st.session_state.max_questions:

    if st.button("Next Question"):
        prompt = generate_question(role, st.session_state.difficulty)
        question = query_ollama(prompt)

        st.session_state.question = question
        st.session_state.question_count += 1
        
if st.session_state.question:
    st.subheader("🧠 Interview Question")
    st.write(st.session_state.question)

    # ------------------------
    # User Answer
    # ------------------------
    answer = st.text_area("Your Answer:")

    if st.button("Submit Answer"):
        if answer:
            eval_prompt = evaluate_answer(st.session_state.question, answer)
            result = query_ollama(eval_prompt)

            # ------------------------
            # Parse Output
            # ------------------------
            score, feedback, improvement = "", "", ""

            try:
                if "SCORE:" in result:
                    parts = result.split("SCORE:")
                    rest = parts[1]

                    if "FEEDBACK:" in rest:
                        score, rest = rest.split("FEEDBACK:")
                    if "IMPROVEMENT:" in rest:
                        feedback, improvement = rest.split("IMPROVEMENT:")
            except:
                st.warning("⚠️ Could not parse response")
                st.write(result)

            # ------------------------
            # Display
            # ------------------------
            tab1, tab2, tab3 = st.tabs(["📊 Score", "📖 Feedback", "🚀 Improvement"])

            with tab1:
                st.metric("Score", score.strip())

            with tab2:
                st.write(feedback.strip())

            with tab3:
                st.write(improvement.strip())