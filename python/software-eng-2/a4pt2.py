def area(x):
    a = x**2

    return a

if __name__ == "__main__":
    x = 4

    print("Square side length:", x)

    a = area(x)

    print("\nThe area of the square is:", a)

    x = 0

    print("Square side length:", x)

    a = area(x)

    print("\nThe area of the square is:", a)

    x = -1

    print("Square side length:", x)

    a = area(x)

    print("\nThe area of the square is:", a)