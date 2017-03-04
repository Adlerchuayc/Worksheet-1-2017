i = input("Please input an integer between 1 and 12  (inclusive) :" + "\n")
k = [x for x in range(1,13)]
print("\n")
print("Multiples of " + i + "\n")
a = 0
while a < 12:
    print(int(i) * k[a])
    a += 1
