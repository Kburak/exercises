def original_reverse(number):
    original = number
    reverseNum = 0
    while(number > 0):
        remainder = number %10
        reverseNum = (reverseNum*10) + remainder
        number = number // 10
    if (original == reverseNum):
        return True
    else:
        return False

print("Original and reverse number is equal")
print(original_reverse(222))