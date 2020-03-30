a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in a:
    if num < 5 :
        print (num)

# Extra
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list =[]

for num in a:
    if num < 5:
        new_list.append(num)
print(new_list)

## Extra 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([num for num in a if num < 5])

## Extra 3

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
n = int(input("Enter a number"))

for num in a:
    if num < n:
        b.append(num)
print(b)
