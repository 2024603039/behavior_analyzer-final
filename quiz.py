import streamlit as st
from utils import load_questions

def run_quiz():
    questions = load_questions()

    score = {
        "plan": 0,
        "delay": 0,
        "avoid": 0,
        "escape": 0,
        "direct": 0,
        "normal": 0,
        "healthy": 0
    }

    st.markdown("## 📋 설문 진행")

    for i, q in enumerate(questions):

        st.markdown(f"""
        <div style="padding:20px;border-radius:15px;background:#1c1f26;margin-bottom:10px;">
        <b>Q{i+1}. {q["question"]}</b>
        </div>
        """, unsafe_allow_html=True)

        answer = st.radio("", list(q["options"].keys()), key=i)

        if answer:
            category = q["options"][answer]
            score[category] += 1

        st.progress((i+1)/len(questions))

    return score