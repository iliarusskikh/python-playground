#Client: A Python script that performs the OAuth 2.0 Authorization Code Flow to access the protected resource.


from requests_oauthlib import OAuth2Session
import webbrowser
import os

# Disable HTTPS enforcement for local testing
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# OAuth 2.0 endpoints for our mock server
authorization_base_url = "http://localhost:5000/authorize"
token_url = "http://localhost:5000/token"
scope = ["read"]  # Example scope

# Client credentials (must match server configuration)
client_id = "my-client-id"
client_secret = "my-client-secret"
redirect_uri = "http://localhost:8000/callback"

# Step 1: Create OAuth2 session
oauth = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

# Step 2: Get authorization URL and prompt user
authorization_url, state = oauth.authorization_url(authorization_base_url)
print(f"Please go to this URL and authorize access: {authorization_url}")
webbrowser.open(authorization_url)

# Step 3: Get the authorization code from the redirect URI
redirect_response = input("Paste the full redirect URL here: ")

# Step 4: Exchange authorization code for access token
token = oauth.fetch_token(
    token_url,
    client_secret=client_secret,
    authorization_response=redirect_response
)

# Step 5: Use the access token to access the protected resource
response = oauth.get("http://localhost:5000/api/resource")
print("API Response:", response.json())
