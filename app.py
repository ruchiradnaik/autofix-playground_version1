# app.py

try:
    from user_service import get_user
except ImportError:
    print("Error: user_service module not found. Please ensure it is installed and available.")
    exit(1)  # Exit the program if the import fails

def main():
    user = get_user(1)
    print("User data:", user)

if __name__ == "__main__":
    main()
# CodeSentinal: created for you by RuchirAdnaik.