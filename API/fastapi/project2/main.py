#uvicorn src.main:app --reload

#These requests are subject to a global rate limit.
#curl -X POST "http://127.0.0.1:8000/chat" \
#     -H "Content-Type: application/json" \
#     -d '{"prompt": "Why is the sky blue?"}'
     
#For a higher rate limit, you can authenticate by providing a JWT token. Make sure to
# replace YOUR_GENERATED_TOKEN with a valid token.

#curl -X POST "http://127.0.0.1:8000/chat" \
#     -H "Content-Type: application/json" \
#     -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsIm5hbWUiOiJKb2huIEpvIiwiaWF0IjoxNTE2MjM5MDIyfQ.dCyjmfsGOG66KxOsbaCMzrhvCjmIgOimQhsISc6BSuE" \
#     -d '{"prompt": "Why is the sky blue?"}'



#The /chat endpoint is protected and requires a JWT token for authentication. For testing
#purposes, you can generate a valid token using jwt.io:

#Algorithm: Change the algorithm to HS256.

#Payload: Use the following payload. The sub field will be used as the user identifier for rate limiting.


#
#eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0dXNlciIsIm5hbWUiOiJKb2huIEpvIiwiaWF0IjoxNTE2MjM5MDIyfQ.dCyjmfsGOG66KxOsbaCMzrhvCjmIgOimQhsISc6BSuE

#Signature: In the "Verify Signature" section, use the secret key
#a-string-secret-at-least-256-bits-long. This is the same secret key that is hardcoded in
#src/auth/dependencies.py.



#valid header
#{
#  "alg": "HS256",
#  "typ": "JWT"
#}

#valid payload
#{
#  "sub": "testuser",
#  "name": "John Jo",
#  "iat": 1516239022
#}

#Sign JTW secret a-string-secret-at-least-256-bits-long
#UTF-8

import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from ai.gemini import Gemini
from auth.dependencies import get_user_identifier
from auth.throttling import apply_rate_limit

load_dotenv()

# --- App Initialization ---
app = FastAPI()


# --- AI Configuration ---
def load_system_prompt():
    try:
        with open("prompts/system_prompt.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None


system_prompt = load_system_prompt()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")


#creating gemini client
ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)


# --- Pydantic Models ---
class ChatRequest(BaseModel):
    prompt: str #expecting a JSON body {"prompt": ""}


class ChatResponse(BaseModel):
    response: str #returning {"response":"..."}


# --- API Endpoints ---
@app.post("/chat", response_model=ChatResponse)#response we return
async def chat(request: ChatRequest, user_id: str = Depends(get_user_identifier)):
    apply_rate_limit(user_id)
    #apply_rate_limit("global_unauthenticated_user")
    response_text = ai_platform.chat(request.prompt)
    #response_text = "Jojo Hallo"
    return ChatResponse(response=response_text)


#test endpoint
@app.get("/")
async def root():
    return {"message": "API is running"}
