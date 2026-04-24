import streamlit as st
import base64

# Function to convert image to base64
def get_base64(img_path):
    with open(img_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64("images/ezhay.jpg")

st.title("🔎 About Me")
st.header("Hola! Welcome to My Portfolio, I'm Ezhay Mei 👋")
st.write("Frontend Learner | UI Designer | Tech Enthusiast")

# Custom CSS
st.markdown(f"""
<style>
.profile-container {{
    display: flex;
    align-items: center;
    gap: 30px;
    margin-bottom: 30px;
}}

.circle-img {{
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
}}

.text {{
    font-size: 16px;
}}

.section {{
    margin-top: 20px;
    margin-bottom: 40px;
}}
</style>

<div class="profile-container">
    <img src="data:image/jpg;base64,{img_base64}" class="circle-img">
    <div class="text">
       Hello! I enjoy developing systems and designing engaging user experiences.<br><br>
       I constantly explore new technologies to improve my skills.
    </div>
</div>
""", unsafe_allow_html=True)

# Education & Goals Section
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("🎓 Education")
st.write("- BS Computer Science, Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology")
st.write("- Trainings in Web Development & Design")

st.subheader("🧩 Goals")
st.write("- Become a skilled Frontend Developer")
st.write("- Advance my skills in HTML, CSS, JavaScript, and frameworks")
st.write("- Build scalable and user-centered web solutions")

st.markdown('</div>', unsafe_allow_html=True)

# Banner 
st.image("images/banner.jpg", use_container_width=True)

st.info("Welcome to my portfolio! Explore my work and skills.")