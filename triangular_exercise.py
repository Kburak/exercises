"""
Write Python function triangular(N) that creates a triangular 2D list of integers. You have to fill the item(row,col) of the list with row*col where 1<=row<= N.
"""
def triangular(N):
    my_list = []
    for row in range(1, N+1):
        list2 = []
        for col in range(1, row + 1):
            list2.append(row*col)
        my_list.append(list2)
    print(*my_list, sep = "\n")

triangular(10)

