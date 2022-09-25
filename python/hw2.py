#1
mins = int(input("Enter the number of minutes: "))

years = mins // 525600
days = int((mins / 525600 - years) * 365)

print(mins, "minutes is approximately", years, "years and", days, "days")

#2
num = int(input("Enter an integer: "))

numofdigits = len(str(num))
def getlastdigit(number):
        return(number%10)

i = 0
while i < numofdigits:
    print(getlastdigit(num))
    num = num // 10
    i += 1

#3
x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))

slope = (y2-y1)/(x2-x1)

print("The slope for the line that connects two points (", x1, ", " , y1, ") and (", x2, ", ", y2, ") is", slope)

#4
investmentamount = float(input("Enter investment amount: "))
yearlyinterestrate = float(input("Enter annual interest rate: "))
numberofyears = float(input("Enter number of years: "))

monthlyinterestrate = yearlyinterestrate / 12
numberofmonths = int(numberofyears * 12)

futureinvestmentamount = investmentamount * (1 + monthlyinterestrate)**numberofyears
print("Accumulated value is", futureinvestmentamount)