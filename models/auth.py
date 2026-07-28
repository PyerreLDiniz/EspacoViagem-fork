import hashlib
import os
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "espaco_viagem.db"


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def init_db() -> str:
    conn = _connect()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()

    admin_exists = conn.execute("SELECT 1 FROM users WHERE username = ?", ("admin",)).fetchone()
    if not admin_exists:
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            ("admin", hash_password("admin123")),
        )
        conn.commit()

    conn.close()
    return str(DB_PATH)


def authenticate_user(username: str, password: str) -> bool:
    init_db()
    conn = _connect()
    try:
        row = conn.execute(
            "SELECT id FROM users WHERE username = ? AND password_hash = ?",
            (username.strip(), hash_password(password)),
        ).fetchone()
        return row is not None
    finally:
        conn.close()


def create_user(username: str, password: str) -> bool:
    if not username or not password:
        return False
    init_db()
    conn = _connect()
    try:
        conn.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username.strip(), hash_password(password)),
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_all_users():
    init_db()
    conn = _connect()
    try:
        return [dict(row) for row in conn.execute("SELECT id, username FROM users ORDER BY id").fetchall()]
    finally:
        conn.close()


def delete_user_by_id(user_id: int) -> bool:
    if not user_id:
        return False
    init_db()
    conn = _connect()
    try:
        cursor = conn.execute("DELETE FROM users WHERE id = ? AND username != ?", (user_id, "admin"))
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()
