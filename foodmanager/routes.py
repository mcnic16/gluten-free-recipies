from flask import render_template
from foodmanager import app, db
from foodmanager.models import Recipe, Food


@app.route("/")
def home():
    return render_template("base.html")