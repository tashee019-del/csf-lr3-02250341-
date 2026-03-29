numbers = [2, 4, 6, 8, 10]
search = int(input("Searching for: "))

for num in numbers:
    if num == search:
        print("Number found")
        break
else:
    print("Number not found")