from flask import Flask, render_template
from second import second


app = Flask(__name__)
app.register_blueprint(second, url_prefix="/admin")#redirects to blueprint file



@app.route("/")#this route is being overriden by second file
def test():
    return "<h1>Test</h1>"


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    


