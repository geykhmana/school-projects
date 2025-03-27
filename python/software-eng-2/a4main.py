from a4pt1 import distance
from a4pt2 import area

print("Assignment 4")
print("Part 1:\n")

x1 = int(input("Enter a value for x1: "))
y1 = int(input("Enter a value for y1: "))
x2 = int(input("Enter a value for x2: "))
y2 = int(input("Enter a value for y2: "))

d = distance(x1, y1, x2, y2)

print("The distance between points 1 and 2 is:", d)

print("\nPart 2:\n")

x = int(input("Enter the side length of a square: "))

a = area(x)

print("Area of the square:", a)