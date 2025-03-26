x1 = int(input("Enter the x value for point 1: "))
y1 = int(input("Enter the y value for point 1: "))

x2 = int(input("Enter the x value for point 2: "))
y2 = int(input("Enter the y value for point 2: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("The distance between the points is: " + str(d))