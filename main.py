# main.py

from calculator import add, divide

def run_operations():
    x = 10
    y = 0  # This will cause an error in calculator.divide

    print("Addition:", add(x, y))
    print("Division:", divide(x, y))  # ❌ Error originates from calculator.py

if __name__ == "__main__":
    run_operations()
