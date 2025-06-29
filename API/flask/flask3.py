#template inheritance

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index1.html", content="Testing")


@app.route("/test")
def test():
    return render_template("new.html")


#@app.route("/<name>")
#def user(name):
#    return render_template("index.html",content=name)
#
#
#@app.route("/admin/")
#def admin():
#    return redirect(url_for("user",name="Admin!"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)


#css bootstrap head https://getbootstrap.com/docs/4.3/getting-started/introduction/
#js at the end of the body
#nav bar bootstrap
