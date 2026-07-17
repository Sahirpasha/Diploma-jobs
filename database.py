
import sqlite3
from pathlib import Path

DB_PATH = Path('database') / 'polymatch.db'
DB_PATH.parent.mkdir(exist_ok=True)

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS jobs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        title TEXT,
        streams TEXT,
        description TEXT,
        location TEXT
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS applications(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_email TEXT,
        job_id INTEGER,
        match_score INTEGER
    )
    ''')

    conn.commit()
    conn.close()
