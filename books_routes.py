from server import fapp, db
from models import Book, PublicationHouse
from flask import jsonify, abort, request

@fapp.route('/api/v1.0/books', methods=['POST'])
def create_book():
    bookdata = request.get_json()
    pubid = bookdata['publication']
    pubObj = PublicationHouse.query.get(pubid)
    b = Book(title=bookdata['title'],price=bookdata['price'],\
        pages=bookdata['pages'], publication=pubObj)

    db.session.add(b)
    db.session.commit()

    return jsonify({
        'id': b.id,
        'title': b.title,
        'pages': b.pages,
        'price': b.price,
        'publication': {
            'id': pubObj.id,
            'title': pubObj.name,
            'ratings': pubObj.ratings
        }
    })
