#1
a = 0
sum = 0
pos = 0
neg = 0
avg = 0
while True:
    num = int(input("\nEnter an integer, entering 0 will end the program: "))
    if num > 0:
        a += 1
        pos += 1
        sum += num
        avg = sum / a
        print("Positive numbers:", pos)
        print("Negative numbers:", neg)
        print("Sum:", sum)
        print("Average:", avg)
    elif num < 0:
        a += 1
        neg += 1
        sum += num
        avg = sum / a
        print("Positive numbers:", pos)
        print("Negative numbers:", neg)
        print("Sum:", sum)
        print("Average:", avg)
    elif num == 0:
        print("\nProgram has ended.")
        break

#2
students = int(input("Enter the number of students: "))
i = 0
names = []
scores = []
if students > 1:
    while i < students:
        name = input("Enter the student's name: ")
        names.append(name)
        score = int(input("Enter the student's score: "))
        scores.append(score)
        i += 1
    highname = names[0]
    highscore = scores[0]
    j = 1
    while j < students:
        if scores[j] > highscore:
            highname = names[j]
            highscore = scores[j]
        j += 1
    print("The student with the highest score was", highname)
    print("The student's score was", highscore)

#3
nums = 100
counter = 0
while nums <= 1000:
    if nums % 5 == 0 and nums % 6 == 0:
        print(nums, end=" ")
        counter += 1
        if counter == 10:
            print("")
            counter = 0
    nums += 1
