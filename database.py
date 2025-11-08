import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site TEXT NOT NULL,
    email TEXT,
    username TEXT,
    encrypted_password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
''')
conn.commit()
conn.close()


def insert_password(site: str, email: str, username: str, encrypted_password: str):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passwords (site, email, username, encrypted_password)
        VALUES (?, ?, ?, ?)                                                 #helps prevent SQL injection
    """, (site, email, username, encrypted_password))
    conn.commit()
    conn.close()

def select_password_by_site(site: str):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT site, email, username, encrypted_password
        FROM passwords
        WHERE site = ?
    """, (site,))