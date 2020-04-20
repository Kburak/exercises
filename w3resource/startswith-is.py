"""
Get a new string from a given string where 'Is' has been added to the front.
If the given string already begins with 'Is' then return the string unchanged
"""
def start_with_is(text):
    if len(text) >= 2 and text[:2] == "Is":
        return text
    return "Is"+text

print(start_with_is("Array"))
print(start_with_is("IsUmit"))

