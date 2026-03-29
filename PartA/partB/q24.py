def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    if choice in [1, 2, 3, 4]:
        a, b = map(int, input("Enter two numbers: ").split())

        if choice == 1:
            print("Sum =", add(a, b))
        elif choice == 2:
            print("Difference =", subtract(a, b))
        elif choice == 3:
            print("Product =", multiply(a, b))
        elif choice == 4:
            print("Quotient =", divide(a, b))
    else:
        print("Invalid choice")