"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
"""


def reverse_word(sentence):
    string_list = sentence.split(" ")
    return " ".join(string_list[::-1])

user_string = input("Please enter a string and i will give it back to you backwards.")

reverse_word(user_string)
