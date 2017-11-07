def readName():
    done = False
    nameL = []
    while not done:
        userInput = input("Enter first, middle, last name, separated by space: ")
        nameL = userInput.split(" ")
        if len(nameL) >= 2:
                done = True
    return nameL;

def changeLast(nameList):
    if nameList[-1].endswith("."):
        lastName = nameList[-2].upper()
    else:
        lastName = nameList[-1].upper()
    return lastName

def main():
    nameList = readName()
    LAST = changeLast(nameList)
    nameList.remove(LAST.lower())
    print(LAST, *nameList)
    

main()
