def how_many_times(text):
    count = 0
    for word in range(len(text)-1):
        count += text[word:word+4] ==  "Emma"
    return count
my_string = "Emma is a good developer. Emma is also a writer"
count = how_many_times(my_string)
print("Emma appeared", count, "times")

# split the words

