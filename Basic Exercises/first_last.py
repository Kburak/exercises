def is_same(num):
    if numlist[0] == numlist[-1]:
        return True
    else:
        return False
numlist = [1,2,3,4,5,1]
print("the first and the last number of a list is same")
print("result is", is_same(numlist))