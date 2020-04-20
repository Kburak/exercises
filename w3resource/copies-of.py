"""
Get a string which is n (non-negative integer) copies of a given string
"""

def copies_func(str,n):
    result = ""

    for text in range(n):
        result += str
    return result

print(copies_func("abc",4))