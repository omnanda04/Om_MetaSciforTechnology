# AI Voice Bot 🗣️

An interactive AI Voice Bot that uses Google's Gemini API for text generation and Google Text-to-Speech for voice output. Built with Streamlit for a user-friendly web interface.

[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://ommetascifortechnology-urr9dyip8mk99zqk6baha7.streamlit.app/)

## 🔗 Live Demo

Try the app here: 👉 [AI Voice Bot Live](https://ommetascifortechnology-urr9dyip8mk99zqk6baha7.streamlit.app/)

---

## Features

- Chat with an AI assistant
- Text-to-speech conversion
- Responsive web interface
- Easy deployment

## Prerequisites

- Python 3.8+
- Google Gemini API key

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai_voice_bot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file:

Copy .env.example to .env

Add your Gemini API key

Running Locally
bash
Copy
Edit
streamlit run app.py
Deployment to Render
Create a new Web Service on Render

Connect your GitHub repository

Set the following environment variables in the Render dashboard:

GEMINI_API_KEY: Your Google Gemini API key

TTS_LANGUAGE: (Optional) Language code (default: 'en')

TTS_SLOW: (Optional) Set to 'true' for slower speech (default: 'false')

Set the build command:

nginx
Copy
Edit
pip install -r requirements.txt
Set the start command:

nginx
Copy
Edit
streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
Deploy!

Usage
Enter your message in the chat input

The AI will respond with text and read it out loud

The conversation history is maintained during your session

Customization
To change the voice speed, modify TTS_SLOW in .env

To change the language, modify TTS_LANGUAGE in .env (e.g., 'es' for Spanish, 'fr' for French)

License
MIT
