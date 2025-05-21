import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
from io import BytesIO
import base64
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Please set your GEMINI_API_KEY in the .env file")
    st.stop()

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Set page config
st.set_page_config(
    page_title="AI Voice Bot",
    page_icon="🗣️",
    layout="wide"
)

def text_to_speech(text, lang='en', slow=False):
    """Convert text to speech using gTTS"""
    tts = gTTS(text=text, lang=lang, slow=slow)
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes

def get_ai_response(prompt):
    """Get response from Gemini"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def main():
    st.title("🤖 AI Voice Bot")
    st.write("Chat with an AI that can talk back to you!")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.spinner("AI is thinking..."):
            response = get_ai_response(prompt)
            
            # Add AI response to chat history and display
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)
                
                # Convert response to speech
                audio_bytes = text_to_speech(
                    response,
                    lang=os.getenv("TTS_LANGUAGE", "en"),
                    slow=os.getenv("TTS_SLOW", "False").lower() == "true"
                )
                
                # Auto-play the audio
                audio_str = "data:audio/ogg;base64,%s" % base64.b64encode(audio_bytes.read()).decode()
                audio_html = f"""
                    <audio autoplay>
                    <source src="{audio_str}" type="audio/ogg">
                    Your browser does not support the audio element.
                    </audio>
                """
                st.components.v1.html(audio_html, height=0)

if __name__ == "__main__":
    main()
