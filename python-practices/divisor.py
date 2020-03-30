number = int(input("Enter a number for its divisors list"))
# to find the numbers up to the given number
number_range = list(range(1,number+1))
divisor_list = []

for num in number_range:
    if number % num == 0:
        divisor_list.append(num)
print(divisor_list)
