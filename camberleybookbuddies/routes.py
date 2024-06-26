from flask import render_template
from camberleybookbuddies import app, db
from camberleybookbuddies.models import Book, Review


@app.route("/")
def home():
    return render_template("base.html")