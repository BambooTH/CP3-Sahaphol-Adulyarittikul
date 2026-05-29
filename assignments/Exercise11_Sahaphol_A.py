Number = int(input("Enter Number: "))
for x in range(Number):
    print(" "*(Number - x -1) + "*"*(2 * x + 1))