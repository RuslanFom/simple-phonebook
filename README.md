# API Semplice Rubrica Telefonica

Questo progetto implementa una semplice API per una rubrica telefonica con operazioni CRUD utilizzando Python, Flask e SQLite.

## Struttura del Progetto

Il progetto è composto da due componenti principali:

1. Server (`server.py`): Implementa gli endpoint API utilizzando Flask e SQLAlchemy.
2. Client (`client.py`): Fornisce funzioni per interagire con l'API.

Struttura dei file:

```
$simple-phonebook/
│
├── server.py
├── client.py
├── requirements.txt
├── README.md
└── .gitignore
```
## Funzionalità

- Creazione di nuovi contatti
- Recupero di tutti i contatti
- Recupero di un contatto specifico tramite ID
- Aggiornamento dei contatti esistenti
- Eliminazione dei contatti


## Installazione

1. Clona il repository:
   ```
   git clone https://github.com/RuslanFom/simple-phonebook.git
   cd simple-phonebook
   ```

2. Crea e attiva un ambiente virtuale:
   ```
   python -m venv venv
   source venv/bin/activate  # Su Windows, usa `venv\Scripts\activate`
   ```

3. Installa i pacchetti richiesti:
   ```
   pip install -r requirements.txt
   ```

## Utilizzo

### Avvio del Server

1. Avvia il server Flask:
   ```
   python server.py
   ```
   Il server sarà in esecuzione su `http://localhost:5000`.

### Utilizzo del Client

Il file `client.py` fornisce funzioni per interagire con l'API. Ecco un esempio di come utilizzarlo:

 ```       
python client.py
 ```      
from client 
 ``` 
import create_contact, get_all_contacts, get_contact, update_contact, delete_contact
 ``` 
Create a new contact
 ``` 
create_contact('John', 'Doe', 'john@example.com', '+1234567890')
 ``` 
Get all contacts
 ``` 
get_all_contacts()
 ``` 
Get a specific contact (assuming ID is 1)
 ``` 
get_contact(1)
 ``` 
Update a contact
 ``` 
update_contact(1, name='Jane', phone='+9876543210')
 ``` 
Delete a contact
 ``` 
delete_contact(1)
 ``` 

## Endpoint API

- `POST /contacts`: Crea un nuovo contatto
- `GET /contacts`: Recupera tutti i contatti
- `GET /contacts/<id>`: Recupera un contatto specifico
- `PUT /contacts/<id>`: Aggiorna un contatto
- `DELETE /contacts/<id>`: Elimina un contatto

## Modello Dati

Ogni contatto ha i seguenti campi:
- `id`: Intero (generato automaticamente)
- `name`: Stringa
- `surname`: Stringa
- `email`: Stringa (unica)
- `phone`: Stringa (unica)

## Gestione degli Errori

L'API restituisce codici di stato HTTP appropriati e messaggi di errore per vari scenari, come:
- 404 Not Found: Quando un contatto richiesto non esiste
- 400 Bad Request: Quando mancano campi obbligatori o sono non validi
