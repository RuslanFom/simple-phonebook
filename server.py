from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phonebook.db'
db = SQLAlchemy(app)

# Modello del contatto
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)

# Creazione della tabella nel database
with app.app_context():
    db.create_all()

# Creazione del contatto
@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.json
    new_contact = Contact(name=data['name'], surname=data['surname'], 
                          email=data['email'], phone=data['phone'])
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({'message': 'Contatto creato', 'id': new_contact.id}), 201

# Ottenimento di tutti i contatti
@app.route('/contacts', methods=['GET'])
def get_all_contacts():
    contacts = Contact.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'surname': c.surname, 
                     'email': c.email, 'phone': c.phone} for c in contacts])

# Ottenimento del contatto per ID
@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get_or_404(id)
    return jsonify({'id': contact.id, 'name': contact.name, 'surname': contact.surname, 
                    'email': contact.email, 'phone': contact.phone})

# Aggiornamento del contatto
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    data = request.json
    contact.name = data.get('name', contact.name)
    contact.surname = data.get('surname', contact.surname)
    contact.email = data.get('email', contact.email)
    contact.phone = data.get('phone', contact.phone)
    db.session.commit()
    return jsonify({'message': 'Contatto aggiornato'})

# Eliminazione del contatto
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    db.session.delete(contact)
    db.session.commit()
    return jsonify({'message': 'Contatto eliminato'})

if __name__ == '__main__':
    app.run(debug=True)