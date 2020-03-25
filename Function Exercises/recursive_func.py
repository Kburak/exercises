def my_func(number):
    if number > 0:
        return number +my_func(number-1)
    else:
        return 0

res = my_func(10)
print(res)
# didn`t get it ask
