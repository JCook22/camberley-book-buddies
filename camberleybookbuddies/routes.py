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


@app.route("/edit_book/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        book.book_title = request.form.get("book_title")
        book.book_author = request.form.get("book_author")
        book.book_genre = request.form.get("book_genre")
        db.session.commit()
        return redirect(url_for("library"))
    return render_template("edit_book.html", book=book)


@app.route("/delete_book/<int:book_id>")
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("library"))


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    library = list(Book.query.order_by(Book.book_title).all())
    if request.method == "POST":
        review = Review(
            book_id=request.form.get("book_id"),
            review_author=request.form.get("review_author"),
            review_headline=request.form.get("review_headline"),
            review_description=request.form.get("review_description")
        )
        db.session.add(review)
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("add_review.html", library=library)


@app.route("/edit_review/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = Review.query.get_or_404(review_id)
    library = list(Book.query.order_by(Book.book_title).all())
    if request.method == "POST":
        review.book_id=request.form.get("book_id")
        review.review_author=request.form.get("review_author")
        review.review_headline=request.form.get("review_headline")
        review.review_description=request.form.get("review_description")
        db.session.commit()
        return redirect(url_for("reviews"))
    return render_template("edit_review.html", review=review, library=library)


@app.route("/delete_review/<int:review_id>")
def delete_review(review_id):
    review = Review.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for("reviews"))


@app.route("/reviews")
def reviews():
    reviews = list(Review.query.order_by(Review.review_headline).all())
    return render_template("reviews.html", reviews=reviews)


@app.route("/contact")
def contact():
    return render_template("contact.html")


