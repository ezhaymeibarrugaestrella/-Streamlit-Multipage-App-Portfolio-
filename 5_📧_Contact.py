import streamlit as st

st.title("📧 Contact Me")

# Contact form inputs
name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

# Send button logic
if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
    else:
        st.error("Please fill all fields.")

# Contact Information
st.markdown("### 📞 Contact Information")
st.write("Name: Ezhay Mei B. Estrella")
st.write("📱 Cellphone: 09636567877")
st.write("📧 Email: ezhaymei.barrugaestrella@gmail.com")

# Social Links section
st.markdown("### 🌐 Social Links")
st.write("- GitHub: https://github.com/ezhaymeibarrugaestrella")
st.write("- Facebook: https://www.facebook.com/share/17ZM6hHKFM/")
st.write("- Instagram: https://www.instagram.com/_u/zzzz.cvz/")