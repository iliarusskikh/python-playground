#pip install flask requests-oauthlib

#Server: A Flask app with:
#/authorize: Authorization endpoint where the user grants access.
#/token: Token endpoint to exchange an authorization code for an access token.
#/api/resource: A protected API endpoint requiring a valid access token.

from flask import Flask, request, jsonify, redirect, url_for, render_template_string
from functools import wraps
import uuid
import time

app = Flask(__name__)

# Simulated database
clients = {
    "my-client-id": {
        "client_secret": "my-client-secret",
        "redirect_uri": "http://localhost:8000/callback"
    }
}
auth_codes = {}  # Temporary storage for authorization codes
tokens = {}     # Storage for access tokens

# Middleware to check for valid access token
def require_oauth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing or invalid token"}), 401
        token = auth_header.split(" ")[1]
        if token not in tokens or tokens[token]["expires_at"] < time.time():
            return jsonify({"error": "Invalid or expired token"}), 401
        return f(*args, **kwargs)
    return decorated

# Authorization endpoint
@app.route("/authorize")
def authorize():
    client_id = request.args.get("client_id")
    redirect_uri = request.args.get("redirect_uri")
    state = request.args.get("state")
    scope = request.args.get("scope")

    print(f"Authorize request: client_id={client_id}, redirect_uri={redirect_uri}, scope={scope}")

    if not client_id or client_id not in clients:
        print("Error: Invalid client_id")
        return jsonify({"error": "Invalid client_id"}), 400
    if not redirect_uri or clients[client_id]["redirect_uri"] != redirect_uri:
        print(f"Error: Invalid redirect_uri. Expected: {clients[client_id]['redirect_uri']}, Got: {redirect_uri}")
        return jsonify({"error": "Invalid redirect URI"}), 400
    if not scope or scope not in ["read"]:
        print("Error: Invalid or missing scope")
        return jsonify({"error": "Invalid or missing scope"}), 400

    # Simulate user login and consent
    auth_code = str(uuid.uuid4())
    auth_codes[auth_code] = {"client_id": client_id, "redirect_uri": redirect_uri}
    print(f"Generated auth_code: {auth_code}")

    return redirect(f"{redirect_uri}?code={auth_code}&state={state}")

# Token endpoint
@app.route("/token", methods=["POST"])
def token():
    client_id = request.form.get("client_id")
    client_secret = request.form.get("client_secret")
    code = request.form.get("code")
    redirect_uri = request.form.get("redirect_uri")

    print(f"Token request: client_id={client_id}, code={code}, redirect_uri={redirect_uri}")

    if (client_id not in clients or
        clients[client_id]["client_secret"] != client_secret or
        code not in auth_codes or
        auth_codes[code]["redirect_uri"] != redirect_uri):
        print("Error: Invalid token request")
        return jsonify({"error": "Invalid token request"}), 400

    # Generate access token
    access_token = str(uuid.uuid4())
    tokens[access_token] = {
        "client_id": client_id,
        "expires_at": time.time() + 3600
    }
    print(f"Generated access_token: {access_token}")

    # Clean up auth code
    del auth_codes[code]

    return jsonify({
        "access_token": access_token,
        "token_type": "Bearer",
        "expires_in": 3600
    })

# Protected API resource
@app.route("/api/resource")
@require_oauth
def protected_resource():
    return jsonify({"message": "This is a protected resource!", "data": {"user_id": 123, "name": "Test User"}})

if __name__ == "__main__":
    app.run(port=5000, debug=True)
