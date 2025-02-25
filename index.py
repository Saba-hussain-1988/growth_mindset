import streamlit as st

# Custom CSS for light pink background
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f0fff0;
        }
        .stApp h1 {
            color: green !important; /* Green Title */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Growth Mind Set Challenge Using Streamlit By S.R.Chohan")
st.text("I am S.R. Chohan, and I have taken on an exciting Growth Mindset Challenge from Sir Zia Khan—to build a web application using Streamlit. This is my very first website, a small yet ambitious effort to step into the world of web development. Let's see how successful this attempt turns out!")
st.header("Why this project?")
st.subheader("💡 A Journey of Growth")
st.text(" – Learning and applying new skills in real-world projects.")
st.subheader("💡 Building with Streamlit")
st.text(" – A simple yet powerful framework for web apps.")
st.subheader("💡 First Step into Web Development")
st.text("– Every great journey begins with a single step!")
st.text("This is just the beginning! Stay tuned as I continue to improve and add new features. Your feedback and support mean the world to me. 🌟")


