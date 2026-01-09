# app.py

from user_service import get_user

def main():
    user = get_user(1)
    print("User data:", user)

main()
