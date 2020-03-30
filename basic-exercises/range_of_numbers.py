def calculate_sum(num):
    previous_num = 0
    for num in range(num):
        sum = previous_num + num
        print(sum)
        previous_num = num


calculate_sum(20)
