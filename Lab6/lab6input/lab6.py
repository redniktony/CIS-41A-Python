#Lab6 - Dictionaries and data structures 
#@Author: Xia Hua

'''
Checker function
@input sets -- string 
@return dictionaries -- whole dictionaries
'''
def checker(name):
    counter = {'A':0,'E':0,'I':0,'O':0,'U':0,'vowel': 0,'total': 0,'percentage':0}
    try:
        with open (name,encoding = "latin-1") as infile:
            for line in infile:
                for char in line:
                    if char.isalpha():
                        counter['total'] += 1 #Calculate the total letters
                    if char.upper() in "AEIOU": 
                        counter[char.upper()] += 1 # Change all vowels to upper and check it 
                        counter["vowel"] += 1 # Add to counter 
    except:
        print("It's not common to have an error in this simple program, genius what did you mess up?")
    counter['percentage'] = counter['vowel'] / counter['total'] #Percentage calculation
    return counter 
'''
Printer function
@input dictionaries -- whole dictionaries
@return N/A -- screen output
''' 
def printer(counter):
    print("A: "+ str(counter['A']))
    print("E: "+ str(counter['E']))
    print("I: "+ str(counter['I']))
    print("O: "+ str(counter['O']))
    print("U: "+ str(counter['U']))
    print("Total vowels / total letters: ", "%.2f"%(counter['percentage']*100)+"%")  # Formatting
'''
Main function
Include all the text files name sets
Pass by reference
'''
def main():
    fileName=("english.txt","french.txt","german.txt","italian.txt","spanish.txt")
    for name in fileName:
        print("")
        print(name[0].upper()+name[1:-4]) # name string ends with '.txt' so use the simple expression like this will good to go
        printer(checker(name))
'''
Run
'''
main()