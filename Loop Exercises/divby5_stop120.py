numlist = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for num in numlist:
    if num % 5 == 0 and num < 120:
        print(num)
    if num > 120 and num % 5 == 0:
        print(num)
        break


