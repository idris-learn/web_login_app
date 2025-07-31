import os
from flask import Flask, render_template, request, redirect, url_for, session
import webbrowser
import threading

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Hardcoded user credentials
users = {
    "mike": "mike@123",
    "essi": "essi@123",
    "kokou": "kokou@123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("welcome"))
        else:
            error = "Invalid credentials"
    return render_template("login.html", error=error)

@app.route("/welcome")
def welcome():
    if "username" in session:
        return render_template("welcome.html", username=session["username"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return render_template("logout.html")

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run()

