import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create a contacts table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        store_name TEXT,
        phone_number TEXT,
        email TEXT,
        address TEXT
    )
''')
conn.commit()

def add_contact(store_name, phone_number, email, address):
    cursor.execute('INSERT INTO contacts (store_name, phone_number, email, address) VALUES (?, ?, ?, ?)', (store_name, phone_number, email, address))
    conn.commit()

def view_contact_list():
    cursor.execute('SELECT store_name, phone_number FROM contacts')
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"Store Name: {contact[0]}, Phone Number: {contact[1]}")

def search_contact(keyword):
    cursor.execute('SELECT store_name, phone_number FROM contacts WHERE store_name LIKE ? OR phone_number LIKE ?', (f'%{keyword}%', f'%{keyword}%'))
    contacts = cursor.fetchall()
    for contact in contacts:
        print(f"Store Name: {contact[0]}, Phone Number: {contact[1]}")

def update_contact(store_name, new_phone_number):
    cursor.execute('UPDATE contacts SET phone_number = ? WHERE store_name = ?', (new_phone_number, store_name))
    conn.commit()

def delete_contact(store_name):
    cursor.execute('DELETE FROM contacts WHERE store_name = ?', (store_name,))
    conn.commit()

# Sample usage
add_contact("Sample Store", "123-456-7890", "sample@store.com", "123 Main St")
view_contact_list()
search_contact("Sample")
update_contact("Sample Store", "987-654-3210")
delete_contact("Sample Store")