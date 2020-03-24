def remove_chars(text,num):
    if len(text)>num:
        return text[num:]
    else:
        return "Number should be less than the length"

print("Removing n number of chars")
print(remove_chars("pynative",4))
#number must be less than the length of string