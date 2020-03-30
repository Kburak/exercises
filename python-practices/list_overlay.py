a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
# to avoid putting same elements to the new list , turned them to a set
for num in set(a):
    if num in set(b):
        c.append(num)

print(c)
     