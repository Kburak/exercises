"""
Accept the base and height of a triangle and compute the area
"""

def triangle_area():
    base = int(input("enter the base: "))
    height = int(input("Enter the height: "))

    area = (base*height) / 2
    print("area:", area)

triangle_area()