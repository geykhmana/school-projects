def distance(x1, x2, y1, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    return d

if __name__ == "__main__":
    x1 = int(input("Enter the x value for point 1: "))
    y1 = int(input("Enter the y value for point 1: "))
    print("\n")
    x2 = int(input("Enter the x value for point 2: "))
    y2 = int(input("Enter the y value for point 2: "))

    d = distance(x1, x2, y1, y2)

    print("\nThe distance between the points is: " + str(d))