#Lab 5 Python 41A
#@Author Xia Hua


'''This function reads the seat data from the file 
@input seatlist
@return seatlist
'''
def readChart(seatList):
    fileName = input("Enter file name or hit Enter for default lab5input2.txt: ")
    if fileName == "": 
        fileName = "lab5input2.txt"
    while len(seatList) == 0:
        try:
            with open(fileName) as infile:
                read = infile.readline()
                if read == "":
                    raise ValueError
                else:
                    seatList.append(read.split())
                    for i in infile:
                        seatList.append(i.split())
        except FileNotFoundError:
            print("The file " + fileName + "can not found in your folder")
            fileName = input("Enter file name or hit Enter for default lab5input2.txt: ")
            if fileName == "" : 
                fileName = "lab5input2.txt"
        except ValueError:
            print(fileName + " is empty.")
            fileName = input("Enter file name or hit Enter for default lab5input2.txt: ")
            if fileName == "" : 
                fileName = "lab5input2.txt"
    return seatList

'''
This function prints data from the seatList
@input seatlist
@return N/A
'''

def printChart(seatList):
    # format for the space title
    print( "%50s" %"Price chart")
    print("%18s" %"Column\n  ",end="")
    #fomat for the row 
    for i in range(len(seatList[0])):
        print("%10d" %(i+1),end="")
    print("\nRow ",end="")
    
    #print the "====" by the length in seatList 
    for i in range(len(seatList[0])):
        print("===========",end="")
    print("")
    
    #fomat for printing the item and values in the list
    for i,line in enumerate(seatList):
        print(i+1,"|",end="")
        for i in line:
            if i == "X" or i == "--":
                print("%10s" %i,end="")
            else:
                print("%10s" %("$" + i),end="")
        print("")
        
'''
This function prints data from the seatList
@input seatList
@return seatList
'''
def buySeat(seatList):
    #By using truple to store the data 
    seatPurchase = []  
    total = 0
    checkInput = 0
    seat = input("\nAvailable seats are shown with price\nEnter row,col for seat " + str(len(seatPurchase) + 1) + " or enter 0 to end: ")
    # Seat checker !!!
    while checkInput !=0:
        try:
            if ',' not in seat:
                raise ValueError
            else:
                checkInput = 1
        except ValueError:
            print("Please enter correct value again")
            
    while seat != '0':
        # For invaild input print info 
        seat = seat.split(sep=',')
        # If user typing the words 
        if not seat[0].strip().isdigit() or not seat[1].strip().isdigit():
            print("Row and column must be numbers")        
        # Search the seat is being taken perviously
        elif (seatList[int(seat[0]) - 1][int(seat[1]) - 1] == 'X') or (seatList[int(seat[0]) - 1][int(seat[1]) - 1]) == '--':
            print("Sorry, that seat is not available.")
        #isdigit input for rows or column
        elif int(seat[0]) < 1 or int(seat[0]) > len(seatList) or int(seat[1]) < 1 or int(seat[1]) > len(seatList[0]):
            print("Invalid row or column")                   
        else:
            # Calcuate the total price for the sold seat 
            total = int(seatList[int(seat[0]) - 1][int(seat[1]) - 1])  + total
            # Reaplce the Price to 'X'
            seatList[int(seat[0]) - 1][int(seat[1]) - 1] = 'X'
            # Using tuple saving the data IMPORTANT!
            seatPurchase.append((int(seat[0]), int(seat[1])))
        #Call again for reinput 
        seat = input("Enter row,col for seat " + str(len(seatPurchase) + 1) + " or enter 0 to end: ")
    
    '''
    Calculate the total price of the ticket that you booked!
    '''
    # Print the total of your purchase 
    print("\nYour total: $", total, sep="")
    print("Your", len(seatPurchase), "seat(s) at ", end='')
    for elem in seatPurchase:
        print(elem,end=' ')
    print("are marked with an 'X'\n")
    return seatList

'''
Save the Chart into files 
@input seatList
@return seatList
'''


def saveChart(seatList):
    fileName = input("Enter file name or hit Enter for default lab5input2.txt: ")
    #By default there will be overwrite input2
    if fileName == "" : 
        fileName = "lab5input2.txt"
    #call outfile open functions 
    with open(fileName,'w') as line :
    #Replace the sold seat by -- and some formating 
        for row in seatList:
            for col in row:
                if col == 'X':
                    line.write("%-4s" %"--")
                else:
                    line.write("%-4s" %col)
            line.write('\n')
    print(fileName + " updated")
'''
Main Function
'''
def main():
    #init a new list for saving data, which use for all functions 
    seatList = []
    #Functions 
    readChart(seatList)
    printChart(seatList)
    buySeat(seatList)
    printChart(seatList) #print tge list again for double check 
    saveChart(seatList) #save
    print ("Done")
'''
Run the main function 
'''
main()
