

def is_prime(number):
    num = int(input("Enter a number"))
    p = [x for x in range(2, num) if num % x == 0]

    if num > 1:
        # checks if the p has any items if true , not prime
        if len(p) == 0:
            return "PRIME NUMBER"
        elif len(p) != 0:
            return "NOT PRIME"
    else:
        return "NOT PRIME"

print(is_prime(number))

