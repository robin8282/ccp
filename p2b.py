from flask import Flask, Response, jsonify, request
import xml.etree.ElementTree as Et 

app = Flask(__name__)

books = [
    {
        'id':1,
        'title':'Book 1',
        'author':'Author Name',
    }, 
    {
        'id':2,
        'title':'Book 2',
        'author':'Author 2'
    }
]

@app.route('/book', methods=['GET'])
def get_all_books():
    root = Et.Element('books')
    for book in books:
        xml_book = Et.SubElement(root, 'book')
        xml_book.set('id', str(book['id']))
        title = Et.SubElement(xml_book, 'title')
        title.text = book['title']
        author = Et.SubElement(xml_book, 'author')
        author.text = book['author']
    xml_string = Et.tostring(root, encoding='utf-8')
    return Response(xml_string, mimetype="text/xml")


@app.route('/book/<int:book_id>', methods=['GET'])
def get_one_book(book_id):
    book = next((b for b in books if b['id']==book_id))
    if book:
        return jsonify(book)
    else:
        return jsonify({"Message": "Book not Found"},404)   

@app.route('/book/add', methods=['POST'])
def add_a_book():
    new_book = {
        'id':len(books)+1,
        'title': request.json['title'],
        'author': request.json['author'],
    }
    books.append(new_book)
    print(books)
    return jsonify(new_book)

@app.route("/book/edit/<int:book_id>",methods=["PUT"])
def update_book(book_id):
    request_data = request.get_json()
    book = next((b for b in books if b['id']==book_id))
    if book:
        book.update(request_data)
        return jsonify(book)
    else:
        return jsonify({"Message":"No Book Found"}), 404

@app.route("/book/remove/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    book = next((bi for bi in books if bi['id'] == book_id))
    if book is None:
        return jsonify({"error":"Book Not Found!"})
    books.remove(book)
    print(books)
    return jsonify({"message":"Successfully removed the book."})

if __name__ == "__main__":
    app.run(debug= True, port=4430)