#Final Exam
#Part A T/F 
'''
1. T
2. T
3. F (Tuple is uncahangeable)
4. T
'''
#Part B (selection problems)
'''
1. D
2. C
3. C
4. B 
'''
#Part C (anlalysis code )
'''
1. ["orange","banana"]
2. X is a list of 10 list, each list is 5 elemets, each element has value 2
3. Each line has at least 2 fields, separated by whitespace
   List
   String 
   dictionary #Index is a string 
'''
#Part D (short and tight space)
'''
1. print(sum([num*num for num in listA]))
2. import math
      def calc():
         c = math.sqrt(a*a + b*b)
         print("%.2f %c)
    
    or we have 
        print(round(c,2))
        
3. try:
      self._numerator = int(numerator)
      self._denominator = int(denominator)
      if self._denominator == 0: rasie ValueError("denominator cannot be 0")
      
4. try:
       myNum = Fraction(input1,input2)
   excpet ValueError as e:
       print(str(e))
except TypeError as e:
       print(str(e))
'''