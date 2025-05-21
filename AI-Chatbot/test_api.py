import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(f"API Key found: {GEMINI_API_KEY[:10]}...")  # Print first 10 chars for security

# Configure Gemini
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content("Say 'Hello, World!'")
    print("\nAPI Test Successful!")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"\nError: {str(e)}")
