from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__="books"
    id = db.Column(db.Integer,primary_key=True)
    isbn = db.Column(db.String,nullable=False)
    title = db.Column(db.String,nullable=False)
    author = db.Column(db.String,nullable =False)
    year = db.Column(db.Integer,nullable=False)


class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    lastname =  db.Column(db.String,nullable=False)
    user = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)

class Review(db.Model):
    __tablename__="reviews"
    id = db.Column(db.Integer,primary_key=True)
    book_id = db.Column(db.Integer,db.ForeignKey("books.id"),nullable=False)
    user_id= db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    review = db.Column(db.String,nullable=False)