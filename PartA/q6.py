print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = int(input("Enter choice: "))
a, b = map(int, input("Enter two numbers: ").split())

if choice == 1:
    print("Sum =", a + b)
elif choice == 2:
    print("Difference =", a - b)
elif choice == 3:
    print("Product =", a * b)
elif choice == 4:
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")