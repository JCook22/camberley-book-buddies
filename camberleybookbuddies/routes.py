from flask import render_template, request, redirect, url_for
from camberleybookbuddies import app, db
from camberleybookbuddies.models import Book, Review


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/library")
def library():
    library = list(Book.query.order_by(Book.book_title).all())
    return render_template("library.html", library=library)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        book = Book(book_title=request.form.get("book_title"), book_author=request.form.get("book_author"), book_genre=request.form.get("book_genre"))
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("add_book"))
    return render_template("add_book.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    return render_template("search.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


