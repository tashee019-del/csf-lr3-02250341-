a, b, c = map(int, input("Enter three numbers: ").split())

if a > b:
    if a > c:
        print(f"{a} is the largest number")
    else:
        print(f"{c} is the largest number")
else:
    if b > c:
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")