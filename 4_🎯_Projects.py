import streamlit as st

st.title("📁 My Projects")

projects = {
    "Web-based Attendance System": "📑 Attendance system with reports (on progress...)",

    "Birthday Card Web": "🧧 Interactive birthday card made in HTML/CSS and JavaScript.\n\n🔗 https://ezhaymeibarrugaestrella.github.io/Teacher-s-Day-Card/\n🔗 https://ezhaymeibarrugaestrella.github.io/birthday-card-for-my-dad/",

    "Barangay Census Small System": "🗃️ Handles barangay census data.\n\n🔗 https://ezhaymeibarrugaestrella.github.io/Brgy.-Census-Survey-System-Web-/",

    "Grading Database System": "📊 Manages student grading data using Microsoft Access.\n\n🔗 https://ezhaymeibarrugaestrella.github.io/Grading-Database-System-ms-access-/",

    "Snake Game": "🐍 Classic snake game built with Python and Turtle.\n\n🔗 https://ezhaymeibarrugaestrella.github.io/Snake-Game-Python-Turtle-/",

    "Sari-sari Store Small System": "🛒 Manages inventory and sales for a small store.\n\n🔗 https://ezhaymeibarrugaestrella.github.io/Sari-Sari-Store-Small-System/"
}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)