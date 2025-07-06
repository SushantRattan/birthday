
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
    <div style='background-color: #fff0f5; padding: 20px; border-radius: 12px; border: 2px solid #ff69b4;'>
        <h3 style='color: #c2185b; font-family: "Segoe UI", sans-serif;'>💝 A Birthday Note Just for You 💝</h3>
        <p style='font-size: 17px; color: #333; font-family: "Segoe UI", sans-serif; line-height: 1.6;'>
            Dear Sabbyyy 🎀,<br><br>

            Today isn't just another day — it's the day the world got a little brighter, a little louder, and a lot more magical ✨<br><br>

            You bring smiles with your chaos, laughter with your jokes, and warmth with your kindness. You're a beautiful mess of sunshine, starlight, and sleepy memes 🌈🌙💬<br><br>

            <strong>Dari jauh, aku kirimkan pelukan virtual dan kue imajiner 🎂</strong> — because you deserve all the love and joy today and every day 💖<br><br>

            <strong>Tetaplah menjadi kamu yang lucu, gila, dan manis.</strong> The world needs more of your kind — unfiltered, funny, and full of heart 😄<br><br>

            <strong>Semoga harimu dipenuhi kejutan manis, tawa lepas, dan momen-momen yang bikin hati hangat.</strong><br>
            May your day be full of sweet surprises, wild laughter, and warm memories ✨<br><br>

            Thank you for being such an amazing online friend, for all the chaos, love, and friendship 🫶🏼<br><br>

            With all my virtual love and Spotify vibes,<br>
            Your goofy buddy,<br>
            Tatan 🧃💖
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
