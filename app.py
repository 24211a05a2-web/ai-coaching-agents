import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Coaching Agent",
    page_icon="📚",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📚 AI Coaching Agent")
page = st.sidebar.radio("Navigate", ["Home", "Upload & Analysis"])

# ================= HOME PAGE =================
if page == "Home":

    st.title("🎯 Personalized Mock Test Coaching System")

    st.write("""
    This AI-powered system analyzes mock test performance,
    identifies weak topics, and generates a structured
    7-day personalized revision plan.
    """)

    st.markdown("### 🚀 Features")
    st.markdown("- Topic-wise Accuracy Analysis")
    st.markdown("- Weak Topic Detection")
    st.markdown("- Performance Evaluation")
    st.markdown("- Study Material Recommendation")
    st.markdown("- Practice Question Generation")
    st.markdown("- AI Doubt Solver")
    st.markdown("- 7-Day Revision Plan Generator")

    st.divider()
    st.caption("🚀 Built for AI Hackathon | Personalized Learning Intelligence System")

# ================= ANALYSIS PAGE =================
elif page == "Upload & Analysis":

    st.title("📊 AI Mock Test Analyzer")
    st.write("Upload your mock test CSV file to generate personalized revision guidance.")

    uploaded_file = st.file_uploader("Upload Mock Test CSV", type=["csv"])

    if uploaded_file is not None:

        # ---------------- DATA PROCESSING ----------------
        df = pd.read_csv(uploaded_file)
        df["Correct"] = df["Student_Answer"] == df["Correct_Answer"]

        topic_accuracy = df.groupby("Topic")["Correct"].mean() * 100

        # ---------------- ACCURACY DISPLAY ----------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Topic Accuracy (%)")
            st.write(topic_accuracy)

        with col2:
            st.subheader("📈 Accuracy Chart")
            st.bar_chart(topic_accuracy)

        st.divider()

        # ---------------- WEAK TOPICS ----------------
        weak_topics = topic_accuracy[topic_accuracy < 60]

        st.markdown("## ⚠ Weak Topics (Below 60%)")

        if weak_topics.empty:
            st.success("🎉 No weak topics detected! Excellent performance.")
        else:
            for topic, score in weak_topics.items():
                st.error(f"{topic} → {score:.2f}% (Needs Improvement)")

        st.divider()

        # ---------------- OVERALL PERFORMANCE ----------------
        overall_score = df["Correct"].mean() * 100

        st.markdown("## 📈 Overall Performance")
        st.metric("Overall Accuracy", f"{overall_score:.2f}%")

        if overall_score < 50:
            st.error("Performance Level: Needs Serious Improvement")
        elif overall_score < 75:
            st.warning("Performance Level: Average - Can Improve")
        else:
            st.success("Performance Level: Good Work! Keep Improving")

        # ---------------- PREDICTED IMPROVEMENT ----------------
        st.markdown("## 📈 Predicted Improvement")

        if overall_score < 60:
            predicted_score = overall_score + 15
        elif overall_score < 80:
            predicted_score = overall_score + 10
        else:
            predicted_score = overall_score + 5

        st.write(f"If you follow the 7-day revision plan, your predicted score can improve to: **{predicted_score:.2f}%**")

        st.divider()

        # ---------------- STUDY MATERIAL ----------------
        study_material = {
            "Algebra": "Revise Algebra formulas + Solve 50 practice problems from NCERT",
            "Trigonometry": "Revise Trigonometry identities + Solve 40 PYQs",
            "Organic Chemistry": "Study Reaction Mechanisms + Practice 30 MCQs",
        }

        st.markdown("## 📚 Recommended Study Materials")

        for topic in weak_topics.index:
            if topic in study_material:
                st.write(f"**{topic}**: {study_material[topic]}")

        st.divider()

        # ---------------- PRACTICE QUESTIONS ----------------
        st.markdown("## 📝 Practice Questions")

        practice_questions = {
            "Algebra": [
                "Solve: 2x + 5 = 15",
                "Find roots of x² - 5x + 6 = 0"
            ],
            "Trigonometry": [
                "Prove sin²θ + cos²θ = 1",
                "Find value of sin 30°"
            ],
            "Organic Chemistry": [
                "Write mechanism of SN1 reaction",
                "Differentiate between SN1 and SN2"
            ]
        }

        for topic in weak_topics.index:
            if topic in practice_questions:
                st.markdown(f"### {topic}")
                for q in practice_questions[topic]:
                    st.write(f"- {q}")

        st.divider()

        # ---------------- 7-DAY PLAN ----------------
        if st.button("Generate 7-Day Revision Plan"):

            st.markdown("## 📅 Your Personalized 7-Day Plan")

            sorted_topics = weak_topics.sort_values()
            plan = []

            for topic in sorted_topics.index:
                plan.append(f"Revise Concepts of {topic}")
                plan.append(f"Practice 40 Questions from {topic}")

            while len(plan) < 6:
                plan.append("Mixed Practice from All Topics")

            plan.append("Full Mock Test and Error Analysis")

            for i in range(7):
                st.write(f"Day {i+1}: {plan[i]}")

            st.divider()

            # ---------------- AI COACHING SUMMARY ----------------
            st.markdown("## 🧠 AI Coaching Summary")

            if weak_topics.empty:
                st.success("Excellent performance! Focus on maintaining consistency.")
            else:
                weakest_topic = weak_topics.idxmin()
                st.info(f"Our AI detected that your weakest area is **{weakest_topic}**. Focus structured revision to improve.")

        st.divider()

        # ---------------- AI DOUBT SOLVER ----------------
        st.markdown("## 💬 AI Doubt Solver")

        user_question = st.text_input("Ask your doubt related to weak topics:")

        if user_question:

            st.write("🤖 AI Response:")

            if "algebra" in user_question.lower():
                st.write("Algebra focuses on solving equations. Remember to isolate the variable and simplify step by step.")
            
            elif "trigonometry" in user_question.lower():
                st.write("In Trigonometry, remember fundamental identities like sin²θ + cos²θ = 1.")
            
            elif "organic" in user_question.lower():
                st.write("In Organic Chemistry, focus on reaction mechanisms and electron movement.")
            
            else:
                st.write("Please ask topic-specific doubts related to your weak areas.")

        st.divider()
        st.caption("🚀 AI-Powered Personalized Learning Intelligence System")

    else:
        st.info("Please upload a CSV file to begin analysis.")