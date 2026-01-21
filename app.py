import streamlit as st

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume")
jd = st.file_uploader("Upload Job Description")

if resume and jd:
    score = calculate_similarity(resume, jd)
    suggestions = generate_suggestions(resume, jd)

    st.metric("Match Score", f"{score}%")
    st.write(suggestions)
