"""
Write a Python program to find whether a given number (accept from the user) is even or odd,
print out an appropriate message to the user.
"""

def even_or_odd():
    number = int(input("Give me a number"))
    if number %2 == 0:
        return number ,"This number is Even"
    else:
        return number , "This number is Odd"

print(even_or_odd())

