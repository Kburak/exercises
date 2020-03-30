"""
my_string = input("Enter a string")

if my_string == my_string[::-1]:
    print("It`s a palindrome")
else:
    print("It`s not a palindrome")
"""
## A better way if its more than 1 word\

my_string = input("Enter a string")
string_list = my_string.split(" ")

for word in string_list:
    if word == word[::-1]:
        print( word , " is a palindrome")
    else:
        print(word , " is not a palindrome")
