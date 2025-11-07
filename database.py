import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site TEXT NOT NULL,
    email TEXT,
    username TEXT,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
''')
conn.commit()
conn.close()


def insert_password(site: str, email: str, username: str, password: str):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (site, email, username, password)
        VALUES (?, ?, ?, ?)                                                 #helps prevent SQL injection
    ''', (site, email, username, password))
    conn.commit()
    conn.close()