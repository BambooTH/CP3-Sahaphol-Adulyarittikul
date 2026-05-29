Number = int(input("Enter Number: "))
for x in range(Number):
    star = " "*(Number - x -1)
    space = "*"*(2* x + 1)
    print(star + space)