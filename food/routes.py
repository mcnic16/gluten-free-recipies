from flask import render_template
from food import app, db
from food.models import Dessert, Recipe


@app.route("/")
def home():
    return render_template("base.html")