import math

def dtb():
    dec = int(input("\nEnter the decimal integer you would like to convert: "))
    bin = ""
    if dec == 0:
        return 0
    elif dec > 0:
        while(dec):
            bin += str(dec&1)
            dec = dec >> 1
        bin = bin[::-1]
        return bin
def btd():
    bin = int(input("\nEnter the binary number you would like to convert: "))
    dec = 0
    binstr = str(bin)
    i = 0
    for x in binstr[::-1]:
        if x == "1":
            dec += 2**i
        i += 1
    return dec

while True:
    choice = input("\nWould you like to convert a decimal number to binary or a binary number to decimal?\n(Type dtb for decimal to binary, btd for binary to decimal, or \"quit\" if you would like to quit the program: ")
    if choice == "quit":
        break
    elif choice == "dtb":
        print(dtb())
    elif choice == "btd":
        print(btd())
    else:
        print("Sorry, I could not understand your input.\n")
