import re
import os

def defaultEval():
    guestExp = re.compile("guest\w+|\w+guest")
    anonExp = re.compile("anonymous [\d|.]+")
    wormExp = re.compile("Worm\.\w+\.\w+-?\w?")
    exeExp = re.compile("\w+\.exe")

    guestMatches = set(guestExp.findall(log))
    anonMatches = set(anonExp.findall(log))
    wormMatches = set(wormExp.findall(log))
    exeMatches = set(exeExp.findall(log))

    print("\nGuest accounts found:")
    print(*guestMatches, sep='\n')
    print("\nAnonymous accounts found:")
    print(*anonMatches, sep='\n')
    print("\nPossible malicious worms found:")
    print(*wormMatches, sep='\n')
    print("\nPossible malicious executables found:")
    print(*exeMatches, sep='\n')
    print("")

    if not guestMatches and not anonMatches:
        print("No guest or anonymous accounts found\n")
    else:
        print("Guest and/or anonymous accounts found.\n")

    if not wormMatches and not exeMatches:
        print("No malicious files found.\n")
    else:
        print("Possible malicious files found.\n")

filename = input("Please enter the path of the file you wish to analyze: ")
while not os.path.isfile(filename):
    print("File not found!\n")
    filename = input("Please enter the path of the file you wish to analyze: ")

with open(filename, 'r') as myfile:
    log = myfile.read().replace('\n', ' ')

choice = input("Enter 1 to use your own custom search pattern or enter 2 to run the default evaluation: ")
while choice != '1' and choice != '2':
    print("Invalid input.\n")
    choice = input("Enter 1 to use your own custom search pattern or enter 2 to run the default evaluation: ")

if choice == '1':
    search = re.compile(input("Enter your search pattern: "))
    matches = set(search.findall(log))
    if matches:
        print("Matches found:")
        print(*matches, sep='\n')
    else:
        print("No matches found.")
else:
    defaultEval()
