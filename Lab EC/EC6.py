# Lab 4:
# Add to the program intName.py in ch 5, section 5 of the book.
# This program turns an integer into its English name.

def intName(number) :
   ''' Turn a number into its English name 
       @param: number (int)
       @return: the name (str)
   '''   
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number. 

   if part >= 100 :
      name = digitName(part // 100) + " hundred"
      part = part % 100

   if part >= 20 :
      name = name + " " + tensName(part)
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0

   if part > 0 :
      name = name + " " + digitName(part)

   return name


def digitName(digit) :
   ''' Turn a digit into its English name
       @param: digit (int)
       @return: name (str)
   '''   
   
   digitDic = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
   if digit in digitDic:    
      return digitDic[digit]
   else:
      return ""
   
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
   value = int(input("Please enter a positive integer < 1000: "))
   print(intName(value))
   
   
# Start the program.
main()
