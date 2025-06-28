# Basic calculator for arithmetic operations
def calculator(a, b, operation):
    if operation == "+": return a + b
    elif operation == "-": return a - b
    elif operation == "*": return a * b
    elif operation == "/": return a / b if b != 0 else "Error: Division by zero"

if __name__ == "__main__":
    a, op, b = input("Enter expression (e.g., 5 + 3): ").split()
    print("Result:", calculator(float(a), float(b), op))