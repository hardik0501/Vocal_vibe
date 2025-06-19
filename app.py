import streamlit as st
import base64
from utils.gemini_api import ask_gemini
from utils.voice import get_voice_input
from utils.emotion import detect_emotion
from gtts import gTTS
import os

st.set_page_config(page_title="VocalVibe AI – Emotional Wellness Assistant", page_icon="🎧")

st.markdown(
    """
    <div style='text-align: center; margin-top: 10px;'>
        <img src='static/logo.png' width='220' style='border-radius: 10px;'/>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<link rel="stylesheet" href="static/style.css">', unsafe_allow_html=True)

st.markdown("<h1 class='header'>🎧 VocalVibe AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='tagline'>Your voice-aware emotional support companion 💜</p>", unsafe_allow_html=True)

mode = st.radio("Choose Input Mode", ["Type", "Voice"], horizontal=True)
user_input = ""

if mode == "Type":
    user_input = st.text_input("How are you feeling today?")
elif mode == "Voice":
    if st.button("🎙️ Speak Now"):
        user_input = get_voice_input()
        st.success(f"You said: {user_input}")

if user_input:
    emotion = detect_emotion(user_input)
    st.session_state.emotion = emotion
    st.info(f"🧠 Emotion Detected: {emotion}")

    if st.button("Ask VocalVibe AI"):
        with st.spinner("Thinking in Hinglish..."):
            response = ask_gemini(user_input)
            st.markdown(f"<div class='response-box'>{response}</div>", unsafe_allow_html=True)

            tts = gTTS(response, lang="hi")
            audio_path = "static/response.mp3"
            tts.save(audio_path)

            with open(audio_path, 'rb') as audio_file:
                audio_bytes = audio_file.read()
                audio_b64 = base64.b64encode(audio_bytes).decode()
                st.markdown(f"""
                <audio autoplay controls>
                    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3">
                </audio>
                """, unsafe_allow_html=True)

mood_videos = {
    "Anxious": {
        "title": "Relaxing Flute Music for Anxiety 🌿",
        "url": "https://www.youtube.com/watch?v=1ZYbU82GVz4"
    },
    "Sad": {
        "title": "Uplifting Hindi Songs to Heal 💜",
        "url": "https://www.youtube.com/watch?v=0UVPbjIhpGg"
    },
    "Positive": {
        "title": "Happy Hindi Playlist ☀️",
        "url": "https://www.youtube.com/watch?v=RRPbZfzpMn0"
    },
    "Neutral": {
        "title": "LoFi Hindi Chill Beats 🎧",
        "url": "https://www.youtube.com/watch?v=iS4tY9S5v8Y"
    }
}

if 'emotion' in st.session_state:
    suggestion = mood_videos.get(st.session_state.emotion, None)
    if suggestion:
        st.markdown(f"""
        <div class="yt-box">
            <h4>🎵 Based on your mood, try this:</h4>
            <a href="{suggestion['url']}" target="_blank" style="font-size:18px;">
                {suggestion['title']} → Watch on YouTube
            </a>
        </div>
        """, unsafe_allow_html=True)

st.image("static/avatar.png", width=200)
