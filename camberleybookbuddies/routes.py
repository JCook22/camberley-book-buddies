from flask import render_template
from camberleybookbuddies import app, db
from camberleybookbuddies.models import Book, Review


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/library")
def library():
    return render_template("library.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    return render_template("add_book.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


