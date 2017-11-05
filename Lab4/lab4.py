# Lab 4:
# Add to the program intName.py in ch 5, section 5 of the book.
# This program turns an integer into its English name.

'''Author: Xia Hua
   Assignment 4
   Due date:  Oct 15
'''

def checkThousand(number):
   '''Under thousand an above thousand Processing Function
      @param number(int)
      @return outputText(string)
   '''   
   digitdata = number
   if (digitdata <0 or digitdata >= 1000000):
      outputText = "input must be between 0 and 1,000,000" 
   elif digitdata >= 1000:
      above_thousand_digitdata = digitdata // 1000 
      under_thousand_digitdata = digitdata % 1000
      outputText = intName(above_thousand_digitdata) + " thousand" + intName(under_thousand_digitdata)
   else:
      outputText = intName(digitdata)
   return outputText
def intName(number) :
   ''' Turn a number into its English name 
       @param: number (int)
       @return: the name (str)
   '''   
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number. 
   # This for the answer genreal processing accpet all numbers
   if part >= 100 :
      name = " "+digitName(part//100)+" hundred"
      part = part % 100
   # This for the answer 100,200,300,400..etc
   if part >= 20:
      if part == 0:  
         return name
   # This for the answer 10,11,12,13,14,15,212,112,117,118...etc (Over 10 under 20)
      else:
         name = name + " " + tensName(part)
         part = part % 10
         if part <10:
            name = name +"-"      
   # This for the answer 21,30,236,130,640,350,860,970,680...etc (Over 20 unedr 100)
   elif part >= 10:
         name = name + " " + teenName(part)
         part = 0       
   # This for the answer 1,2,3,102,203,403...etc(Only digit under 10)
   if part > 0:
      if part == 0:
         return name
      if name.endswith('-'):
         name = name + digitName(part)
         return name 
      name = name + " " + digitName(part)
   return name

'''
String Library -- 1
'''
def digitName(digit) :
   ''' Turn a digit into its English name
       @param: digit (int)
       @return: name (str)
   '''   
   if digit == 1 : return "one"
   if digit == 2 : return "two"
   if digit == 3 : return "three"
   if digit == 4 : return "four"
   if digit == 5 : return "five"
   if digit == 6 : return "six"
   if digit == 7 : return "seven"
   if digit == 8 : return "eight"
   if digit == 9 : return "nine"
   return ""

'''
String Library -- 2
'''
def teenName(number) :
   ''' Turn a number between 10 and 19 into its English name
       @param: number (int)
       @return: name (str)
   '''   
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "fifteen"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   return ""

'''
String Library -- 3
'''
def tensName(number) :
   ''' Turn a number between 20 and 99 into its English name
       @param: number (int)
       @return: name (str)
   '''   
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""

def main() :
   value = 1
   print("Lab 4: Functions")
   while(value != 0 ):
      value = int(input("Please enter a positive integer < 1,000,000 (or 0 to end): ")) #input digit
      print(checkThousand(value).lstrip()) #name = name.lstrip() by using this methods will delete the space in front.
   print("Program ends...")

'''
Main function call
'''
main()

'''
OutPut
Lab 4: Functions
Please enter a positive integer < 1,000,000 (or 0 to end): -3
input must be between 0 and 1,000,000
Please enter a positive integer < 1,000,000 (or 0 to end): 1000
one thousand
Please enter a positive integer < 1,000,000 (or 0 to end): 987654
nine hundred eighty-seven thousand six hundred fifty-four
Please enter a positive integer < 1,000,000 (or 0 to end): 300003
three hundred thousand three
Please enter a positive integer < 1,000,000 (or 0 to end): 300300
three hundred thousand three hundred
Please enter a positive integer < 1,000,000 (or 0 to end): 300333
three hundred thousand three hundred thirty-three
Please enter a positive integer < 1,000,000 (or 0 to end): 333444
three hundred thirty-three thousand four hundred forty-four
Please enter a positive integer < 1,000,000 (or 0 to end): 333404
three hundred thirty-three thousand four hundred four
Please enter a positive integer < 1,000,000 (or 0 to end): 12
twelve
Please enter a positive integer < 1,000,000 (or 0 to end): 10001
ten thousand one
Please enter a positive integer < 1,000,000 (or 0 to end): 2000000
input must be between 0 and 1,000,000
Please enter a positive integer < 1,000,000 (or 0 to end): 0

Program ends...
'''