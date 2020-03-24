def even_func(text):
    for char in range(0,len(text)-1,2):
        print("index[char]",text[char])

my_string = input("Enter String")
print("Original string is ", my_string)
print("Printing only even index chars")
even_func(my_string)