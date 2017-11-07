#@Author Xia Hua
#Midterm questions

def readName():
    checker = False 
    while not checker:
        name= input("Please type your full name, use space to seperate.").split(' ')
        if len(name) < 2:
            print("Try again. FirstName Middle Name Last Name. Don't include space in the end.")
        else:
            checker = True
    return name

def nameThread(nameList):
    lastName = nameList[-1]
    if lastName[-1] == '.':
        optionalSuffix = lastName
        lastName = nameList[-2]
        checker = 1
    else:
        checker = 0
    lastName = lastName.upper()
    return (lastName,checker)

def main():
    nameList = readName()
    first = nameList[0]
    nameList.pop(0)
    LASTtuple = nameThread(nameList)
    if LASTtuple[1] == 1:
        optional_suffix = nameList[-1]
        nameList.pop(-1)
    else:
        optional_suffix = ' '
    LAST = LASTtuple[0]
    nameList.pop(-1)
    optional_middle =''.join(str(x) for x in nameList)
    print(LAST+",",first,optional_middle,optional_suffix)
main()
    



