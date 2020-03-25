def outer_func(a, b):
    def inner_func(a, b):
        return a+b
    return inner_func(a, b) + 5
result = outer_func(5,15)
print(result)