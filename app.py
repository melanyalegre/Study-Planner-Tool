import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="Study Planner AI", page_icon="📚")

# -------------------------------
# Title Section
# -------------------------------
st.title("📚 Study Planner Tool")
st.write("A simple AI-inspired tool to help you plan your study time based on difficulty and upcoming deadlines.")

# -------------------------------
# Instructions
# -------------------------------
st.subheader("How it works")
st.markdown("""
1. Enter your **subjects** (one per line).  
2. Use the **slider** to set how hard each subject is (1 = very easy, 5 = very hard).  
3. Fill in how many **days until the exam** for each subject.  
4. Choose how many hours you can study this week and which days you’re available.  
5. Click **Generate Study Plan** to get a suggested allocation.
""")

# -------------------------------
# Subjects input
# -------------------------------
st.subheader("Subjects")

subjects_raw = st.text_area(
    "Enter your subjects (one per line):",
    value="Math\nEconomics\nStatistics",
    height=120
)

subject_names = [s.strip() for s in subjects_raw.split("\n") if s.strip()]

# -------------------------------
# Sliders and days for each subject
# -------------------------------
data = []

if subject_names:
    st.subheader("Set difficulty and days until exam")

    for i, name in enumerate(subject_names):
        col1, col2 = st.columns(2)

        with col1:
            diff = st.slider(
                f"Difficulty: {name}",
                min_value=1,
                max_value=5,
                value=3,
                step=1,
                key=f"diff_{i}"
            )

        with col2:
            days_left = st.number_input(
                f"Days until exam: {name}",
                min_value=0.0,
                value=7.0,
                step=1.0,
                key=f"days_{i}"
            )

        data.append(
            {
                "Subject": name,
                "Difficulty": float(diff),
                "Days_left": float(days_left),
            }
        )
else:
    st.info("Add at least one subject above to configure difficulty & days.")

# -------------------------------
# Global study settings
# -------------------------------
total_hours = st.number_input(
    "Total study hours you have this week:",
    min_value=1.0,
    max_value=168.0,
    value=15.0,
    step=1.0
)

if total_hours > 58:
    st.warning("Studying more than 100 hours a week may be unrealistic. Pace yourself.")



days_options = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
study_days = st.multiselect("Which days can you study?", days_options, default=days_options[:5])

# -------------------------------
# Generate Plan Button
# -------------------------------
if st.button("Generate Study Plan"):
    if not data:
        st.warning("Please enter at least one subject.")
        st.stop()

    df = pd.DataFrame(data)

    # Priority score: difficulty / (days left + 1)
    df["Priority_score"] = df["Difficulty"] / (df["Days_left"] + 1)

    total_score = df["Priority_score"].sum()
    if total_score == 0:
        st.error("All priority scores are zero. Check your difficulty and days inputs.")
        st.stop()

    df["Hours_assigned"] = df["Priority_score"] / total_score * total_hours
    df["Hours_assigned"] = df["Hours_assigned"].round(1)

    st.subheader("📘 Your Study Plan")
    st.dataframe(df)

    # Chart
    st.subheader("📊 Hours per Subject")
    chart_df = df[["Subject", "Hours_assigned"]].set_index("Subject")
    st.bar_chart(chart_df)

    # Weekly Schedule
    st.subheader("🗓 Weekly Schedule Suggestion")

    if len(study_days) == 0:
        st.warning("You didn’t select any study days.")
    else:
        schedule = []
        n_days = len(study_days)

        for _, row in df.iterrows():
            hours_each_day = row["Hours_assigned"] / n_days
            for day in study_days:
                schedule.append({
                    "Day": day,
                    "Subject": row["Subject"],
                    "Hours": round(hours_each_day, 1)
                })

        sched_df = pd.DataFrame(schedule)
        st.dataframe(sched_df)

        st.success("Your study plan has been generated!")
