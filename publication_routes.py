from server import fapp, db
from models import PublicationHouse
from flask import jsonify, abort, request

@fapp.route('/api/v1.0/publication-houses', methods=['POST'])
def create_pub_house():
    pubdata = request.get_json()

    p = PublicationHouse(**pubdata)
    db.session.add(p)
    db.session.commit()

    return jsonify({
        'id': p.id,
        'name': p.name,
        'ratings': p.ratings
    })

@fapp.route('/api/v1.0/publication-houses/<int:pub_id>', methods=['GET'])
def get_pub_house(pub_id):
    p = PublicationHouse.query.get(pub_id)
    books = [{
        'id': book.id,
        'title': book.title,
        'price': book.price,
        'pages': book.pages
    }for book in p.books]

    return jsonify({
        'id': p.id,
        'name': p.name,
        'ratings': p.ratings,
        'books': books
    })
