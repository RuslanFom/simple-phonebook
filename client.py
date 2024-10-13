import requests

BASE_URL = 'http://localhost:5000'

# Funzione per creare un nuovo contatto
def create_contact(name, surname, email, phone):
    response = requests.post(f'{BASE_URL}/contacts', json={
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone
    })
    print(response.json())

# Funzione per ottenere tutti i contatti
def get_all_contacts():
    response = requests.get(f'{BASE_URL}/contacts')
    print(response.json())

# Funzione per ottenere un contatto specifico per ID
def get_contact(id):
    response = requests.get(f'{BASE_URL}/contacts/{id}')
    print(response.json())

# Funzione per aggiornare un contatto specifico per ID
def update_contact(id, name=None, surname=None, email=None, phone=None):
    data = {}
    if name: data['name'] = name
    if surname: data['surname'] = surname
    if email: data['email'] = email
    if phone: data['phone'] = phone
    response = requests.put(f'{BASE_URL}/contacts/{id}', json=data)
    print(response.json())

# Funzione per eliminare un contatto specifico per ID
def delete_contact(id):
    response = requests.delete(f'{BASE_URL}/contacts/{id}')
    print(response.json())

# Esempio di utilizzo
if __name__ == '__main__':
    # Creazione di un contatto
    create_contact('Mario', 'Rossi', 'mario.rossi@example.com', '+393757654321')
    
    # Ottenimento di tutti i contatti
    get_all_contacts()
    
    # Ottenimento di un contatto specifico per ID (supponiamo che ID = 1)
    get_contact(1)
    
    # Aggiornamento di un contatto
    update_contact(1, name='Pietro', phone='+393757654321')
    
    # Eliminazione di un contatto
    delete_contact(1)
