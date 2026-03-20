def generate_question(role, difficulty):
    return f"""
You are an expert interviewer.

Generate ONE {difficulty} level interview question for the role: {role}

Make it relevant and realistic.
"""

def evaluate_answer(question, answer):
    return f"""
You are an expert interviewer.

Evaluate the candidate's answer.

Question:
{question}

Answer:
{answer}

Respond STRICTLY in this format:

SCORE: <0-10>

FEEDBACK:
<what was good and bad>

IMPROVEMENT:
<how to improve>
"""