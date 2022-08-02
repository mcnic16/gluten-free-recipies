from flask import render_template
from foodmanager import app, db



@app.route("/")
def home():
    return render_template("home.html")
