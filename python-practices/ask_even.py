number = int(input("Enter a number"))

if number % 4 == 0:
    print(number , " is even and is multiple of 4")
elif number %2 == 0:
    print(number , " is even")
else:
    print(number , " is odd")

## extra
num = int(input("Enter a num"))
check = int(input("Enter another num"))

if num % check == 0 :
    print(num , "divides evenly by" , check)
else:
    print(num , "doesn`t divide evenly by" , check)