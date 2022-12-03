#1
def reverse(num):
    i = 1
    lenofstr = len(str(num))
    while i <= lenofstr:
        lastdigit = int(num % 10)
        print(lastdigit, end="")
        i += 1
        num -= lastdigit
        num = num / 10

reverse(int(input("Enter an integer: ")))

print("\n")

#2
def displaysortednumbers(num1, num2, num3):
    nums = []
    nums.append(num1)
    nums.append(num2)
    nums.append(num3)
    nums.sort()
    print("The sorted numbers are:", end=" ")
    for j in nums:
        print(j, end=" ")

num1 = float(input("Enter number1: "))
num2 = float(input("Enter number2: "))
num3 = float(input("Enter number3: "))
displaysortednumbers(num1, num2, num3)