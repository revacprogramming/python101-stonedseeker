# 3
# 0.0 0.0 0.0 1.0 1.0 0.0
# -1.0 2.0 3.0 5.0 1.0 1.0
# 5.0 9.0 -0.5 0.0 7.5 5.0
# Resultant output
# ----------------
# Area of rectangle with vertices (0.0,0.0),(0.0,1.0),(1.0,0.0) is 1.0
# Area of rectangle with vertices (-1.0,2.0),(3.0,5.0),(1.0,1.0) is 10.0
# Area of rectangle with vertices (5.0,9.0),(-0.5,0.0),(7.5,5.0) is 44.5
# 1

# class Rectangles:
#     def input(self,side):
#         self.side = side
#         number_of_rectangles = int(input("Enter the number os triangles\n"))
#         for i in range(number_of_rectangles):
#             ,b,c = int(input("Enter the three sides of the trian"))

##learning classes 

# class Door:
#     def __init__(self):
#         self.name = input("Enter name")
#         self.age = input("enter age")

from re import L
from unicodedata import name


def number_of_sides():
    number_of_sides = int(input('Enter the number of sides'))
    return number_of_sides


def input(sides: int):
    a,b,c,d = input("Enter the coordinates of rectangle").split()

def main(): 
    sides = number_of_sides()
    coordinates = input(sides)


if __name__ == "__main__":
    main()
