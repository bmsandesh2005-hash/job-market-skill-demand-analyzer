"""Streamlit starter dashboard using demo data until a real dataset is supplied."""
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Job Market Skill Analyzer", page_icon="📊", layout="wide")
st.title("AI-Powered Job Market and Skill Demand Analyzer")
st.caption("Educational starter dashboard — demo data is illustrative, not real market evidence.")

demo = pd.DataFrame([
    {"title": "Data Analyst", "location": "Bengaluru", "description": "Python, SQL, Excel, Power BI, communication skills"},
    {"title": "Junior Data Scientist", "location": "Bengaluru", "description": "Python, machine learning, statistics, Pandas, NumPy"},
    {"title": "Business Analyst", "location": "Hyderabad", "description": "SQL, Excel, Tableau, communication"},
    {"title": "ML Intern", "location": "Remote", "description": "Python, machine learning, NLP, Git, AWS"},
    {"title": "BI Analyst", "location": "Pune", "description": "SQL, Power BI, Excel, data analysis"},
])

uploaded = st.file_uploader("Upload a job-postings CSV (optional)", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.success("CSV loaded. Showing available columns and a preview.")
else:
    df = demo
    st.info("Showing five illustrative demo records. Upload your own permitted dataset for actual analysis.")

st.subheader("Dataset preview")
st.dataframe(df, use_container_width=True)
st.metric("Records loaded", len(df))

if "title" in df.columns:
    st.subheader("Job titles")
    st.bar_chart(df["title"].fillna("Unknown").value_counts())

if "location" in df.columns:
    st.subheader("Locations")
    st.bar_chart(df["location"].fillna("Unknown").value_counts())

if "description" in df.columns:
    from src.analyze_jobs import extract_skills
    skills = [skill for value in df["description"].fillna("").astype(str) for skill in extract_skills(value)]
    if skills:
        st.subheader("Skill mentions in loaded descriptions")
        st.bar_chart(pd.Series(skills).value_counts())
    else:
        st.warning("No skill mentions detected. Confirm the CSV has a description column.")
st.caption("Keyword matching is a starter method and should be validated before drawing conclusions.")
