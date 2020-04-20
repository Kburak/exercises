"""Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
Return the n copies of the whole string if the length is less than 2
"""

def copies_of(str,n):
    result = ""
    for text in range(n):
        if len(str) < 2:
            result += str
        else:
            result += str[:2]
    return result

print(copies_of('p', 2))