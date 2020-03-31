"""
This function gives you the nth fibonacci number

"""


def Fibonacci_check(n):
    if n <= 0:
        print("Incorrect input")
    elif n > 300:
        print("This program only goes up to 300")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci_check(n - 1) + Fibonacci_check(n - 2)


if __name__ == '__main__':
    print(Fibonacci_check(10))
