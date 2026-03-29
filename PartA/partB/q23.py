def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(f"{i} -> {check_even_odd(i)}")