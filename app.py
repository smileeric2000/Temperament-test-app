import streamlit as st
from questions import questions
from score_logic import calculate_temperament, get_dominant_temperament
from utils import generate_pdf_report


def intro():
    st.markdown(
        """
        <div style='text-align: center; padding: 2rem;'>
            <h1 style='color: #4B9CD3;'>🧠 Discover Your Temperament</h1>
            <p style='font-size: 1.1rem; color: #909090;'>
                Welcome to the <strong>Temperament Personality Test</strong> – a fun, insightful quiz designed to help you learn more about your natural behavior patterns, emotional tendencies, and social interactions.
            </p>
            <hr style='margin: 2rem 0;' />
            <h3 style='color: #6C63FF;'>📋 How It Works</h3>
            <ul style='text-align: left; max-width: 600px; margin: auto; font-size: 1.05rem;'>
                <li>💬 You’ll be asked <strong>20 questions</strong> about your behavior, reactions, and preferences.</li>
                <li>📊 At the end, we’ll analyze your answers and show you your <strong>dominant temperament</strong>.</li>
                <li>📄 You can optionally <strong>download your results</strong> as a PDF report.</li>
            </ul>
            <hr style='margin: 2rem 0;' />
            <p style='font-size: 1rem; color: #808080;'>
                Are you ready to learn more about yourself?
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.button("🚀 Start the Test", on_click=lambda: st.session_state.update({"page": 1}))
    st.markdown("</div>", unsafe_allow_html=True)


st.set_page_config(page_title="Temperament Test", layout="centered")

if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(questions)
if "page" not in st.session_state:
    st.session_state.page = 0

# def intro():
#     st.title("🧠 Temperament Test")
#     st.write("Welcome! This test will help you discover your dominant temperament based on your responses to 20 questions.")
#     if st.button("Start Test"):
#         st.session_state.page += 1

def questionnaire():
    q = questions[st.session_state.page - 1]
    st.subheader(f"Question {st.session_state.page}: {q['question']}")
    st.session_state.answers[st.session_state.page - 1] = st.radio(
        "Choose one:",
        list(q["options"].keys()),
        index=0 if st.session_state.answers[st.session_state.page - 1] is None else
        list(q["options"].keys()).index(st.session_state.answers[st.session_state.page - 1])
    )

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.page -= 1
    if col2.button("Next"):
        if st.session_state.page < len(questions) + 1:
            st.session_state.page += 1
        else:
            st.session_state.page += 1  #Go to results page

def results():
    mapped_answers = []
    for i, ans in enumerate(st.session_state.answers):
        temperament = questions[i]["options"].get(ans)
        if temperament:
            mapped_answers.append(temperament)
    
    score = calculate_temperament(mapped_answers)
    dominant = get_dominant_temperament(score)

    st.title("🎉 Your Temperament Result")
    if dominant:
        st.subheader(f"Dominant Temperament: {dominant}")
        descriptions = {
            "Choleric": "Natural leader, goal-oriented, confident.",
            "Sanguine": "Lively, social, expressive, people-person.",
            "Melancholic": "Thoughtful, analytical, often reserved.",
            "Phlegmatic": "Calm, steady, peaceful, diplomatic."
        }
        st.write(descriptions[dominant])

        if st.download_button("📄 Download Report", file_name=f"{dominant}_report.pdf",
                              data=open(generate_pdf_report("User", dominant, descriptions[dominant]), "rb").read()):
            st.success("Report downloaded.")
    else:
        st.warning("Couldn't determine your temperament. Please complete all questions.")

# Page routing
if st.session_state.page == 0:
    intro()
elif 1 <= st.session_state.page <= len(questions):
    questionnaire()
else:
    results()
