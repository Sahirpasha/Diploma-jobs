
import bcrypt
from database import get_connection

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_user(name, email, password, role):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            'INSERT INTO users(name,email,password,role) VALUES (?,?,?,?)',
            (name, email, hash_password(password), role)
        )
        conn.commit()
        return True, 'Registration successful'
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT name,password,role FROM users WHERE email=?', (email,))
    row = cur.fetchone()
    conn.close()

    if row and verify_password(password, row[1]):
        return {'name': row[0], 'role': row[2], 'email': email}
    return None
