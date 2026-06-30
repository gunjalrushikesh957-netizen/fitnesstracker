import streamlit as st
import pandas as pd
from database import save_data, get_data

st.set_page_config(
    page_title="Fitness Tracker",
    page_icon="🏃",
    layout="wide"
)

st.title("🏃 Fitness Tracker App")
st.write("Track your daily fitness activities")

st.header("Daily Fitness Log")

steps = st.number_input("👣 Steps Walked", min_value=0)

exercise = st.selectbox(
    "🏋️ Exercise Type",
    ["Walking", "Running", "Cycling", "Gym", "Yoga", "Other"]
)

minutes = st.number_input("⏱ Workout Time (Minutes)", min_value=0)

calories = st.number_input("🔥 Calories Burned", min_value=0)

if st.button("💾 Save Data"):
    save_data(steps, exercise, minutes, calories)
    st.success("✅ Data Saved Successfully!")

st.divider()

st.header("📊 Dashboard")

data = get_data()

if data:

    df = pd.DataFrame(
        data,
        columns=["ID", "Steps", "Exercise", "Minutes", "Calories"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("👣 Total Steps", int(df["Steps"].sum()))
    col2.metric("⏱ Total Minutes", int(df["Minutes"].sum()))
    col3.metric("🔥 Total Calories", int(df["Calories"].sum()))

    st.subheader("📋 Saved Records")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Steps Chart")
    st.bar_chart(df["Steps"])

    st.subheader("🔥 Calories Chart")
    st.line_chart(df["Calories"])

else:
    st.info("No records found. Please save your first fitness record.")