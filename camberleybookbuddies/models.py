from camberleybookbuddies import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    book_author = db.Column(db.String(50), nullable=False)
    book_genre = db.Column(db.String(20), nullable=False)
    reviews = db.relationship(
        "Review", backref="book", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.book_title


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        "book.id", ondelete="CASCADE"), nullable=False)
    review_author = db.Column(db.String(50), nullable=False)
    review_headline = db.Column(db.String(75), nullable=False)
    review_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"#{self.id} - Headline:{self.review_headline}"
