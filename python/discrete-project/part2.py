def dtb():
    dec = int(input("Enter the decimal integer you would like to convert: "))
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
    bin = int(input("Enter the binary number you would like to convert: "))

while True:
    choice = input("Would you like to convert a decimal number to binary or a binary number to decimal?\n(Type dtb for decimal to binary, btd for binary to decimal, or \"quit\" if you would like to quit the program: ")
    if choice == "quit":
        break
    elif choice == "dtb":
        print(dtb())
    elif choice == "btd":
        btd()
    else:
        print("Sorry, I could not understand your input.\n")
