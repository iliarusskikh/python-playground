#sessions
#pip install --upgrade Flask-Session Flask-Login
from flask import Flask, redirect, url_for, render_template, request, session
from flask_session import Session

from datetime import timedelta #permanent sessions

app = Flask(__name__)
#app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(seconds=30)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'hello'
Session(app)

@app.route("/")
def home():
    return render_template("index1.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True #session timeout
        user = request.form["nm"]
        session["user"]= user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
            
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

    

if __name__ == "__main__":
    app.run(debug=True, port=8000)


