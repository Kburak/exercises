def is_divisible(numlist):
    for num in numlist:
        if num %5 == 0:
            print(num)
numlist = [1,2,3,4,5,6,7,8,9,10]
print("Finding divisible of 5 in a list")
is_divisible(numlist)