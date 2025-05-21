import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from io import BytesIO
import base64
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("❌ GEMINI_API_KEY not found. Please set it in .env or Streamlit Secrets.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Streamlit app config
st.set_page_config(page_title="AI Voice Bot", page_icon="🗣️", layout="centered")

# Text to speech
def text_to_speech(text, lang='en', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

# Gemini response
def get_ai_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error generating response: {str(e)}"

# Main Streamlit app
def main():
    st.title("🤖 AI Voice Bot")
    st.markdown("Chat with an AI that talks back using Gemini + gTTS")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display past chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # New user input
    if prompt := st.chat_input("Type your message here..."):
        # Show user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI response
        with st.spinner("AI is thinking..."):
            response = get_ai_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

                # Convert response to audio
                audio_bytes = text_to_speech(
                    response,
                    lang=os.getenv("TTS_LANGUAGE", "en"),
                    slow=os.getenv("TTS_SLOW", "False").lower() == "true"
                )

                # Embed audio in HTML
                audio_base64 = base64.b64encode(audio_bytes.read()).decode()
                audio_html = f"""
                    <audio autoplay>
                        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                """
                st.components.v1.html(audio_html, height=0)

if __name__ == "__main__":
    main()
