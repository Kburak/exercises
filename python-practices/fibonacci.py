def fibonacci(number):
    num = int(input("How many fibonacci numbers would you like to generate? "))
    n = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1, 1]
    elif num > 2:
        fib = [1, 1]
        while n < (num - 1):
            fib.append(fib[n] + fib[n - 1])
            n += 1

    return fib

print(fibonacci(num))


# Better version ust sinir