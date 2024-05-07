import sqlite3

class Database:
    def __init__(self, db_name="database.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT UNIQUE,
                            password TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS beers (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            rating INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS locations (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            rating INTEGER)''')
        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        self.conn.commit()

    def get_user_by_username(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return self.cursor.fetchone()

    def insert_beer(self, name, rating):
        self.cursor.execute("INSERT INTO beers (name, rating) VALUES (?, ?)", (name, rating))
        self.conn.commit()

    def insert_location(self, name, rating):
        self.cursor.execute("INSERT INTO locations (name, rating) VALUES (?, ?)", (name, rating))
        self.conn.commit()
