from server import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50))
    done = db.Column(db.Boolean)

class PublicationHouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ratings = db.Column(db.Integer, nullable=True)
    books = db.relationship('Book', backref='publication')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    pages = db.Column(db.Integer, nullable= True)
    publication_id = db.Column(db.Integer, db.ForeignKey('publication_house.id'))

# ph.books
# book.publication
