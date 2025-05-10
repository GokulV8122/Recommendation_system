import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace this with your actual processed DataFrame)
f_id = "1_N-b2PEFZeENKZu_V6Bmi9AOrs0pknVh"
url = f"https://drive.google.com/uc?export=download&id={f_id}"
df = pd.read_excel(url, parse_dates=True, engine='openpyxl')

st.set_page_config(page_title="Student Retention Dashboard", layout="wide")
st.title("📊 Student Engagement & Retention Dashboard")

# Sidebar for student selection
st.sidebar.header("🔍 Select Student")
student_names = df["First Name"].unique()
selected_student = st.sidebar.selectbox("Choose a student:", student_names)

# Function to generate recommendations
def generate_recommendations(row):
    name = row.get("First Name", "Student")
    gender = row["Gender"]
    country = row["Country"]
    engagement = row["Engagement Rate"]
    timing = row["Application Timing"]
    opp_timing = row["Opportunity Timing Category"]
    duration = row["Engagement Duration Category"]

    title = f"📌 Recommendations for {name} ({gender}, {country})"
    recs = []

    # Engagement-based
    if engagement == 0.0:
        recs.append("🧭 Initiate weekly check-ins to improve engagement.")
        recs.append("📈 Provide guided pathways for onboarding.")
    elif engagement < 0.5:
        recs.append("📊 Assign peer mentors to improve learning consistency.")
        recs.append("🧩 Gamify learning content for better motivation.")
    else:
        recs.append("🌟 Encourage peer leadership roles for continued engagement.")

    # Application timing
    if timing == "Late":
        recs.append("⏰ Send early application nudges and deadline alerts.")
    else:
        recs.append("✅ Recognize early applicants through digital badges.")

    # Opportunity timing
    if opp_timing == "Late":
        recs.append("📅 Align opportunity start times with academic schedules.")

    # Engagement duration
    if duration == "Low":
        recs.append("🎯 Suggest bite-sized learning content.")
        recs.append("📚 Encourage participation in short-term challenges.")
    elif duration == "High":
        recs.append("🧠 Recommend capstone or leadership opportunities.")

    return title, recs

# Display personalized recommendations
if selected_student is not None:
    student_data = df[df["First Name"] == selected_student].iloc[0]
    title, recs = generate_recommendations(student_data)

    st.subheader(title)
    for rec in recs:
        st.write(rec)

