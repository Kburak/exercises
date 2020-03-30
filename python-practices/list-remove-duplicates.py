"""
Write a program (function!) that takes a list and returns a new list that
 contains all the elements of the first list minus all the duplicates.

 Extras:
-Write two different functions to do this - one using a loop and constructing a list, and another using sets.
-Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

#using for loop
def remove_duplicates(list):
    unique_list  = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


print(remove_duplicates([1,2,3,4,5,6,6,6,7,7]))

# using sets
def duplicates(new):
    return list(set(new))


print(duplicates([1,2,3,4,5,6,6,6,7,7,8,8]))