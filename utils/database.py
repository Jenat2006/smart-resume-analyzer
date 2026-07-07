import sqlite3


DATABASE_NAME = "resume.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME, timeout=30)


def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Resume History Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        filename TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


# ==========================
# Register User
# ==========================

def register_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users(name,email,password)
        VALUES(?,?,?)
        """,
        (name, email, password)
    )

    conn.commit()
    conn.close()


# ==========================
# Login User
# ==========================

def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM users
        WHERE email=? AND password=?
        """,
        (email, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================
# Save Resume
# ==========================

def save_resume(email, filename, score):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resumes(email,filename,score)
        VALUES(?,?,?)
        """,
        (email, filename, score)
    )

    conn.commit()
    conn.close()


# ==========================
# Resume History
# ==========================

def get_resume_history(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT filename, score
        FROM resumes
        WHERE email=?
        ORDER BY id DESC
        """,
        (email,)
    )

    history = cursor.fetchall()

    conn.close()

    return history