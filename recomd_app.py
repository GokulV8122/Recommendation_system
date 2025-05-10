import streamlit as st
import pandas as pd

# Load dataset from Google Drive
f_id = "1_N-b2PEFZeENKZu_V6Bmi9AOrs0pknVh"
url = f"https://drive.google.com/uc?export=download&id={f_id}"
df = pd.read_excel(url, parse_dates=True, engine='openpyxl')

# Streamlit page config
st.set_page_config(page_title="Student Retention Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .big-title {
            font-size: 40px;
            font-weight: bold;
            color: #004d99;
        }
        .highlight-box {
            background-color: #e6f0ff;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-size: 18px;
        }
        .rec-card {
            background-color: #f9f9f9;
            border-left: 6px solid #1a75ff;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            margin-top: 20px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>📊 Student Engagement & Retention Dashboard</div>", unsafe_allow_html=True)
st.markdown("-----")

# Sidebar
st.sidebar.header("🔍 Select Student")
student_names = df["First Name"].unique()
selected_student = st.sidebar.selectbox("Choose a student:", student_names)

# Engagement level categorization
def get_engagement_category(rate):
    if rate == 0:
        return "None"
    elif rate < 0.3:
        return "Low"
    elif rate < 0.7:
        return "Moderate"
    else:
        return "High"

# Recommendation logic
def generate_recommendations(row):
    name = row.get("First Name", "Student")
    gender = row["Gender"]
    country = row["Country"]
    engagement = row["Engagement Rate"]
    timing = row["Application Timing"]
    opp_timing = row["Opportunity Timing Category"]
    duration = row["Engagement Duration Category"]
    engagement_category = get_engagement_category(engagement)

    st.markdown(f"<div class='section-title'>📌 Recommendations for <strong>{name}</strong> ({gender}, {country})</div>", unsafe_allow_html=True)

    # Highlight box for engagement
    st.markdown(f"""
        <div class='highlight-box'>
            <strong>🧭 Engagement Level:</strong> <span style='color:#1a75ff'>{engagement_category}</span><br>
            <strong>📈 Engagement Rate:</strong> {engagement:.2f}
        </div>
    """, unsafe_allow_html=True)

    # Engagement-based
    st.markdown("<div class='section-title'>🎯 Engagement</div>", unsafe_allow_html=True)
    if engagement == 0.0:
        st.markdown("<div class='rec-card'>🧭 Initiate weekly check-ins to improve engagement.</div>", unsafe_allow_html=True)
        st.markdown("<div class='rec-card'>🧩 Provide onboarding mentorship for support.</div>", unsafe_allow_html=True)
    elif engagement < 0.3:
        st.markdown("<div class='rec-card'>🎮 Introduce gamified learning and leaderboard.</div>", unsafe_allow_html=True)
        st.markdown("<div class='rec-card'>🔔 Push regular engagement alerts.</div>", unsafe_allow_html=True)
    elif engagement < 0.7:
        st.markdown("<div class='rec-card'>👥 Invite to peer learning communities.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='rec-card'>🌟 Assign leadership or ambassador roles.</div>", unsafe_allow_html=True)
        st.markdown("<div class='rec-card'>🧑‍🏫 Encourage peer-led sessions.</div>", unsafe_allow_html=True)

    # Application timing
    st.markdown("<div class='section-title'>⏰ Application Timing</div>", unsafe_allow_html=True)
    if timing == "Late":
        st.markdown("<div class='rec-card'>⏳ Send early deadline reminders.</div>", unsafe_allow_html=True)
        st.markdown("<div class='rec-card'>🏅 Offer early-bird incentives.</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='rec-card'>✅ Recognise timely applicants with badges.</div>", unsafe_allow_html=True)

    # Opportunity Timing
    st.markdown("<div class='section-title'>📅 Opportunity Timing</div>", unsafe_allow_html=True)
    if opp_timing == "Late":
        st.markdown("<div class='rec-card'>📆 Align opportunity dates with academic calendars.</div>", unsafe_allow_html=True)

    # Engagement Duration
    st.markdown("<div class='section-title'>⏳ Engagement Duration</div>", unsafe_allow_html=True)
    if duration == "Low":
        st.markdown("<div class='rec-card'>📚 Suggest short-term learning sprints.</div>", unsafe_allow_html=True)
        st.markdown("<div class='rec-card'>🧩 Promote interactive, bite-sized tasks.</div>", unsafe_allow_html=True)
    elif duration == "High":
        st.markdown("<div class='rec-card'>🎓 Recommend leadership and capstone projects.</div>", unsafe_allow_html=True)

# Display section
if selected_student:
    student_data = df[df["First Name"] == selected_student].iloc[0]
    generate_recommendations(student_data)
