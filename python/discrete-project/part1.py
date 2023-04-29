def findPrimes(a, b):
    primetest = a   #primetest is each number in the range [a,b] that will be tested to see it it's prime
    i = 0           #index of list of prime numbers
    primelist = []  #list of prime numbers
    while primetest <= b:
        isprime = True  #number is assumed to be prime because 1 & 2 can't be tested, so they are automatically added to primelist
        divisor = 2     #lowest divisor tested is 2 because every number is divisible by 1
        while divisor < primetest:  #loop stops at 2 possible conditions: all divisors from 2 to primetest-1 are tested...
            if primetest % divisor == 0:
                isprime = False
                primetest += 1
                break               #...or the number has been found to not be prime
            else:
                divisor += 1
        if isprime == True:         #code in this condition runs unless number is not prime
            primelist.insert(i, primetest)
            i += 1
            primetest += 1
    print("\nThe prime numbers between these two numbers are:") #printing the prime numbers
    for x in primelist:
        print(x, end=" ")

while True:
    print("This program will find every prime number between two integers that you enter (inclusive)\n")
    a = int(input("Enter the lower bound: "))
    b = int(input("Enter the upper bound: "))
    findPrimes(a, b)
    print("\n\n")