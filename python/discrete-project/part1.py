def findPrimes(a, b):
    primetest = a
    i = 0
    primelist = []
    while primetest <= b:
        isprime = True
        divisor = 2
        while divisor < primetest:
            if primetest % divisor == 0:
                primetest += 1
                divisor = 2
                isprime = False
                continue
            else:
                divisor += 1
        if isprime == True:
            primelist.insert(i, primetest)
            i += 1
            primetest += 1
    print("\nThe prime numbers between these two numbers are:")
    for x in primelist:
        print(x, end=" ")

while True:
    print("This program will find every prime number between two integers that you enter (inclusive)\n")
    a = int(input("Enter the lower bound: "))
    b = int(input("Enter the upper bound: "))
    findPrimes(a, b)
    print("\n\n")