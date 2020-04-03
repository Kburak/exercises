"""
Create a password generator, use main method
"""
import random


def password_gen():

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXCYZ123456789!@#$%^&*()"
    number = int(input("Number of passwords? "))
    length = int(input("Password length"))

    for pw in range(number):
        password = ""
        for char in range(length):
            password += random.choice(chars)
        print(password)

if __name__ == '__main__':
    password_gen()

