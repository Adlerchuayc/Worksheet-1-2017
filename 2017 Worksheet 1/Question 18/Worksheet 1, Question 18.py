ins10c = int(input("Enter the number of 10-cent coins inserted:" + "\n"))
ins20c = int(input("Enter the number of 20-cent coins inserted:" + "\n"))
ins50c = int(input("Enter the number of 50-cent coins inserted:" + "\n"))
ins1d = int(input("Enter the number of 1-dollar coins inserted:" + "\n"))

price = float(input("Please enter either the price of the drink, i.e., 0.8 or 1.2:" + "\n"))

totalins = ins10c * 0.1 + ins20c * 0.2 + ins50c * 0.5 + ins1d

print("Total inserted: $" + str(totalins))

change = totalins - price
print("The machine returns a total of $" + str(change) + ", in the form of:")

ret1d = 0
ret50c = 0
ret20c = 0
ret10c = 0

while change >= 1:
    ret1d += 1
    change -= 1

while change >= 0.5:
    ret50c += 1
    change -= 0.5

while change >= 0.2:
    ret20c += 1
    change -= 0.2

while change > 0:
    ret10c += 1
    change -= 0.1


print(str(ret1d) + " x 1-dollar coin(s)")
print(str(ret50c) + " x 50-cent coin(s)")
print(str(ret20c) + " x 20-cent coin(s)")
print(str(ret10c) + " x 10-cent coin(s)")
