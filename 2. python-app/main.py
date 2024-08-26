n = int(input("Please enter number: "))

if n < 0:
    print("Error: number must be positive")
else:
    sum = 0
    i = n
    while i > 0:
        sum += i
        i -= 1
    print("Sum of all positive numbers till", n, "is", sum)