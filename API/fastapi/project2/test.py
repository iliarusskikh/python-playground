#uvicorn test:app --reload
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

def send_prompt_to_gemini(prompt: str) -> str:
    """
    Sends a prompt to the Gemini model and returns the response.
    
    Args:
        prompt (str): The text prompt to send to the Gemini model.
    
    Returns:
        str: The response from the Gemini model.
    
    Raises:
        Exception: If the API call fails.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: Failed to get response from Gemini API: {str(e)}"

def main():
    # Example prompt
    prompt = "Write a short poem about the beauty of a starry night."
    
    # Send the prompt and print the response
    response = send_prompt_to_gemini(prompt)
    print("Prompt:", prompt)
    print("Response:", response)

if __name__ == "__main__":
    main()




#from fastapi import FastAPI
#from dotenv import load_dotenv
#import os
#
#load_dotenv()
#
#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#if not GEMINI_API_KEY:
#    raise ValueError("GEMINI_API_KEY environment variable not set.")
#
#app = FastAPI()
#
#@app.get("/")
#async def root():
#    return {"message": "Hello, World!"}
