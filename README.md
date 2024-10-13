# Simple Phonebook API

This project implements a simple phonebook API with CRUD operations using Python, Flask, and SQLite.

## Project Structure

The project consists of two main components:

1. Server (`server.py`): Implements the API endpoints using Flask and SQLAlchemy.
2. Client (`client.py`): Provides functions to interact with the API.

## Features

- Create new contacts
- Retrieve all contacts
- Retrieve a specific contact by ID
- Update existing contacts
- Delete contacts

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/simple-phonebook.git
   cd simple-phonebook
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

1. Start the Flask server:
   ```
   python server.py
   ```
   The server will run on `http://localhost:5000`.

### Using the Client

The `client.py` file provides functions to interact with the API. Here's an example of how to use it:

python
from client import create_contact, get_all_contacts, get_contact, update_contact, delete_contact
Create a new contact
create_contact('John', 'Doe', 'john@example.com', '+1234567890')
Get all contacts
get_all_contacts()
Get a specific contact (assuming ID is 1)
get_contact(1)
Update a contact
update_contact(1, name='Jane', phone='+9876543210')
Delete a contact
delete_contact(1)


## API Endpoints

- `POST /contacts`: Create a new contact
- `GET /contacts`: Retrieve all contacts
- `GET /contacts/<id>`: Retrieve a specific contact
- `PUT /contacts/<id>`: Update a contact
- `DELETE /contacts/<id>`: Delete a contact

## Data Model

Each contact has the following fields:
- `id`: Integer (auto-generated)
- `name`: String
- `surname`: String
- `email`: String (unique)
- `phone`: String (unique)

## Error Handling

The API returns appropriate HTTP status codes and error messages for various scenarios, such as:
- 404 Not Found: When a requested contact doesn't exist
- 400 Bad Request: When required fields are missing or invalid

## Future Improvements

- Add authentication and authorization
- Implement pagination for large datasets
- Add more advanced search and filtering options
- Implement input validation and sanitization


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
