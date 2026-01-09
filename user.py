# user_service.py

from database import connect_db

def get_user(user_id):
    db = connect_db()
    return db.get("users")[user_id]   # ❌ ERROR: db is None
