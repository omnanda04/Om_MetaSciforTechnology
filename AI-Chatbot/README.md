# AI Voice Bot 🗣️

An interactive AI Voice Bot that uses Google's Gemini API for text generation and Google Text-to-Speech for voice output. Built with Streamlit for a user-friendly web interface.

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
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key

## Running Locally

```bash
streamlit run app.py
```

## Deployment to Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables in the Render dashboard:
   - `GEMINI_API_KEY`: Your Google Gemini API key
   - `TTS_LANGUAGE`: (Optional) Language code (default: 'en')
   - `TTS_SLOW`: (Optional) Set to 'true' for slower speech (default: 'false')
4. Set the build command:
   ```
   pip install -r requirements.txt
   ```
5. Set the start command:
   ```
   streamlit run app.py --server.port=$PORT --server.address=0.0.0.0 --server.headless=true
   ```
6. Deploy!

## Usage

1. Enter your message in the chat input
2. The AI will respond with text and read it out loud
3. The conversation history is maintained during your session

## Customization

- To change the voice speed, modify `TTS_SLOW` in `.env`
- To change the language, modify `TTS_LANGUAGE` in `.env` (e.g., 'es' for Spanish, 'fr' for French)

## License

MIT
