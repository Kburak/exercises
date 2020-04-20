"""
Count the number 4 in a given list
"""

def count_4(numlist):
    count = 0
    for num in numlist:
        if num == 4:
            count += 1
    return count

print(count_4([1,3,4,4,5,6,4,4,4]))

