while True:
    choice = input("Would you like to convert a decimal number to binary or a binary number to decimal?\n(Type dtb for decimal to binary, btd for binary to decimal, or \"quit\" if you would like to quit the program: ")
    if choice == "quit":
        break
    elif choice == "dtb":
        dtb()
    elif choice == "btd":
        btd()
    else:
        print("Sorry, I could not understand your input.\n")