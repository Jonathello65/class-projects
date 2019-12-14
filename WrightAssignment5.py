# CIS120-401
# Assignment #5
# Jonathan Wright
longestRow = -1
while longestRow != 0:
    longestRow = eval(input("Enter the number of the row you want to be the longest. Enter 0 to end input: "))

    maxStars = (longestRow * 2) - 1
    star = "*"
    numberOfSpaces = longestRow - 1

    for i in range(1, maxStars + 1, 2):
        for k in range(0, numberOfSpaces):
            print(" ", end=' ')
        for j in range(0, i):
            print(star, end=' ')
        for k in range(0, numberOfSpaces):
            print(" ", end=' ')
        print()
        numberOfSpaces -= 1

    maxStars -= 2

    for i in range(maxStars, 0, -2):
        numberOfSpaces += 1
        for k in range(0, numberOfSpaces + 1):
            print(" ", end=' ')
        for j in range(0, i):
            print(star, end=' ')
        for k in range(0, numberOfSpaces):
            print(" ", end=' ')
        print()