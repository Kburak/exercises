def merge_list(list1,list2):
    thirdlist = []
    for num in list1:
        if num %2 != 0:
            thirdlist.append(num)
    for num in list2:
        if num % 2 == 0:
            thirdlist.append(num)
    return thirdlist

print("Merged list is")
list1 =[10, 20, 23, 11, 17]
list2 =[13, 43, 24, 36, 12]

print(merge_list(list1,list2))


