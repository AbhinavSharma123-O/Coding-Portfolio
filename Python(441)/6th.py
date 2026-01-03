def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
terms = int(input("Enter Fibonacci terms"))
print("Fibonacci Series:")
if terms <= 0:
    print("enter")
else:
    for i in range(terms):
        print(fibonacci_recursive(i), end=" ")
