def distance(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    return d

if __name__ == "__main__":
    x1 = 2
    y1 = 3
    print("Point 1: (" + str(x1) + ", " + str(y1) + ")")
    x2 = 7
    y2 = 5
    print("Point 2: (" + str(x2) + ", " + str(y2) + ")")

    d = distance(x1, x2, y1, y2)

    print("\nThe distance between the points is:", d) # Expected answer: 2.23606797749979

    x1 = 1
    y1 = 1
    print("Point 1: (" + str(x1) + ", " + str(y1) + ")")
    x2 = 1
    y2 = 1
    print("Point 2: (" + str(x2) + ", " + str(y2) + ")")

    d = distance(x1, x2, y1, y2)

    print("\nThe distance between the points is:", d)  # Expected answer: 0

    x1 = 7
    y1 = 8
    print("Point 1: (" + str(x1) + ", " + str(y1) + ")")
    x2 = 4
    y2 = 6
    print("Point 2: (" + str(x2) + ", " + str(y2) + ")")

    d = distance(x1, x2, y1, y2)

    print("\nThe distance between the points is:", d)  # Expected answer: 2.23606797749979