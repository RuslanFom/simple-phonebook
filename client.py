import requests

BASE_URL = 'http://localhost:5000'

def create_contact(name, surname, email, phone):
    response = requests.post(f'{BASE_URL}/contacts', json={
        'name': name,
        'surname': surname,
        'email': email,
        'phone': phone
    })
    print(response.json())

def get_all_contacts():
    response = requests.get(f'{BASE_URL}/contacts')
    print(response.json())

def get_contact(id):
    response = requests.get(f'{BASE_URL}/contacts/{id}')
    print(response.json())

def update_contact(id, name=None, surname=None, email=None, phone=None):
    data = {}
    if name: data['name'] = name
    if surname: data['surname'] = surname
    if email: data['email'] = email
    if phone: data['phone'] = phone
    response = requests.put(f'{BASE_URL}/contacts/{id}', json=data)
    print(response.json())

def delete_contact(id):
    response = requests.delete(f'{BASE_URL}/contacts/{id}')
    print(response.json())

# Пример использования
if __name__ == '__main__':
    # Создание контакта
    create_contact('Иван', 'Иванов', 'ivan@example.com', '+79123456789')
    
    # Получение всех контактов
    get_all_contacts()
    
    # Получение контакта по ID (предположим, что ID = 1)
    get_contact(1)
    
    # Обновление контакта
    update_contact(1, name='Петр', phone='+79987654321')
    
    # Удаление контакта
    delete_contact(1)