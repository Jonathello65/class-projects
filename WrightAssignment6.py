# CIS120-401
# Jonathan Wright
# Assignment #6


def isValid(number):
    if getSize(number) < 13 or getSize(number) > 16:
        return False
    elif (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 != 0:
        return False
    else:
        return True


def sumOfDoubleEvenPlace(number):
    number = int(str(number)[::-1])
    sum = 0
    length = getSize(number)
    for i in range(1, length, 2):
        x = getDigit(int(str(number)[i]) * 2)
        sum += x
    return sum


def getDigit(number):
    if number < 10:
        return number
    else:
        return number + (number - 10)


def sumOfOddPlace(number):
    number = int(str(number)[::-1])
    sum = 0
    length = getSize(number)
    for i in range(0, length, 2):
        sum += int(str(number)[i])
    return sum


# def prefixMatched(number, d):


def getSize(d):
    return len(str(d))


def getPrefix(number, k):
    length = getSize(number)
    if length < k:
        return number
    else:
        return number[0-k]

def main():
    number = eval(input("Please enter a credit card number: "))
    if isValid(number) == True:
        print("The credit card is valid.")
    else:
        print("The credit card is invalid.")

main()