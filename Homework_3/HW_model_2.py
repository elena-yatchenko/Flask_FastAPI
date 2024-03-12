from flask_sqlalchemy import SQLAlchemy

# from datetime import datetime
# import enum

db = SQLAlchemy()


class Author(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String, nullable=False)
    author_lastname = db.Column(db.String, nullable=True)
    books = db.relationship("Book", backref=db.backref("author_reference"), lazy=True)

    def __repr__(self):
        return f"Author({self.author_name}, {self.author_lastname})"


class Book(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    public_year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id_"), nullable=False)

    def __repr__(self):
        return f"Book({self.name}, {self.public_year}, {self.author_id})"
