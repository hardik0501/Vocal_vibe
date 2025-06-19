# 🎧 VocalVibe AI – Your Emotional Wellness Companion

Welcome to **VocalVibe AI**, an empathetic web app designed to support your emotional wellness. Whether you're feeling down, anxious, or just want to share how you feel, VocalVibe AI provides a safe space to talk, receive understanding feedback, and get mood-lifting music suggestions.

---

## 🌐 Tech Stack

| Component         | Role/Description                        |
|-------------------|-----------------------------------------|
| **Streamlit**     | Interactive Web UI                      |
| **Gemini Flash**  | AI-generated emotional responses        |
| **gTTS**          | Hindi (Hinglish) Text-to-Speech         |
| **Emotion Classifier** | Detects emotion from user input    |
| **Base64 Audio**  | Plays voice feedback in-browser         |
| **YouTube**       | Suggests mood-appropriate videos        |
| **CSS**           | Modern, calming UI styling              |

---

## 💡 Objective

- **Empathetic Conversation:** Users can freely type or speak about their emotional state.
- **AI Responses:** Receive an understanding, empathetic reply in Hinglish, both as text and soothing voice.
- **Mood-Based Music:** Get personalized YouTube music/video recommendations to match or improve your mood.

---

## 🧩 Key Features

### 1. User Input Modes

- **Type:** Enter your feelings in a text box.
- **Voice:** Speak directly to the app using built-in voice recording.

```python
mode = st.radio("Choose Input Mode", ["Type", "Voice"])
```

### 2. Emotion Detection

- Your input is analyzed using a custom `detect_emotion()` function.
- Detected emotion (e.g. "Sad", "Anxious", "Neutral", "Positive") is stored in the session for use across the app.

```python
emotion = detect_emotion(user_input)
st.session_state.emotion = emotion
```

### 3. Gemini API Response

- Input is sent to Gemini Flash via `ask_gemini(user_input)`.
- The empathetic response is:
  - Shown in a styled message box
  - Converted to a soothing Hinglish voice using gTTS
  - Played back as an embedded audio clip

```python
response = ask_gemini(user_input)
tts = gTTS(response, lang="hi")
tts.save(audio_path)
```

### 4. Audio Playback

- The generated `.mp3` is base64-encoded and played directly in the browser for a seamless voice experience.

```python
<audio autoplay controls>
    <source src="data:audio/mp3;base64,...">
</audio>
```

### 5. Mood-Based YouTube Suggestions

- After emotion detection, the app suggests a relevant YouTube music/video link to help lift your spirits.

```python
mood_videos = {
    "Sad": { "title": "Relaxing Uplift", "url": "..." },
    ...
}
<a href="{url}" target="_blank">Watch on YouTube</a>
```

### 6. Visual Interface

- **Custom Logo:** `logo.png` centered at the top
- **CSS Styling:** Uses `style.css` for soft, modern, and calming aesthetics
  - Custom fonts for headers
  - Styled response and video boxes

---

## 🧠 Workflow (End-to-End)

```
User types or speaks
        ↓
Emotion is detected
        ↓
Gemini replies empathetically
        ↓
Voice is generated and played
        ↓
Mood-based music/video is recommended
```

---

## 🚀 Getting Started

1. **Clone the repository**
2. **Install dependencies:**  
   `pip install -r requirements.txt`
3. **Run the app:**  
   `streamlit run app.py`
4. **Enjoy a calming, supportive experience!**

---

## 📁 File Structure

```
.
├── app.py
├── logo.png
├── style.css
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

We welcome contributions to enhance VocalVibe AI! Please open issues or submit PRs for suggestions or improvements.

---

## 🛡️ Disclaimer

VocalVibe AI is intended for casual emotional support and is not a substitute for professional mental health care.

---

## 📢 Contact

For questions, feedback, or collaborations, please open an issue or reach out via the repository.

---
