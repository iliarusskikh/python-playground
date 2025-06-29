#pip install flask-sqlalchemy
#database
from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_session import Session
from datetime import timedelta #permanent sessions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes=30)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
Session(app)

db = SQLAlchemy(app)

class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email




@app.route("/")
def home():
    return render_template("index7.html")



@app.route("/view")
def view():
    return render_template("view8.html", values=Users.query.all())



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True #session timeout
        user = request.form["nm"]
        session["user"]= user
        
        found_user = Users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            usr = Users(user, None)
            db.session.add(usr)
            db.session.commit()
            
        
        flash("Login successful!")

        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
            
        return render_template("login7.html")



@app.route("/user", methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        
        if request.method == "POST":
            email = request.form["email"]
            session["email"]= email
            found_user = Users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved!")

        else:
            if "email" in session:
                email = session["email"]
        
        return render_template("user7.html", email=email)#passing user to html
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))



@app.route("/logout")
def logout():
    #if "user" in session:
    #    user = session["user"]
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)

    return redirect(url_for("login"))

    

if __name__ == "__main__":
    with app.app_context():  # Add application context
        db.create_all()
    app.run(debug=True, port=8000)
    


