
import streamlit as st
import base64

# Page config
st.set_page_config(page_title="🎀 Sabbyyy's Birthday Surprise", layout="centered")

# Title and emojis
st.markdown("<h1 style='text-align: center; color: #d63384;'>🎉 Happy Birthday Sabbyyy 🎉</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>💖🌸✨💐🌷❤️</h3>", unsafe_allow_html=True)

# Show image
st.image("sabbyyy_beach.jpg", caption="Sabbyyy at the beach 🏖️", use_container_width=True)


# Button to reveal message

if st.button("💌 Open My Message"):
    st.markdown("""
    <div style='background-color: #fff0f5; padding: 20px; border-radius: 10px; border: 2px solid #ff69b4;'>
        <h3 style='color: #d63384;'>💝 A Birthday Note Just for You 💝</h3>
        <p style='font-size: 16px;'>
        ...
        </p>
    </div>
    """, unsafe_allow_html=True)




# Background music
def add_bg_music(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
        b64 = base64.b64encode(audio_bytes).decode()
        st.markdown(f'''
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        ''', unsafe_allow_html=True)

add_bg_music("happy.mp3")
