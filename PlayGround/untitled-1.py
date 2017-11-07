#for i in range (-2,2,2):
#    for j in range(3):
#        print (j)
'''
def functionA(name, number = 4 ,location = "De Anza"):
    print (name, number,location)
    
def main ():
    functionA("Python")
    
main()
'''

'''
var1 = "num"
var2 = 998.237
print("%s: #%2.2f" % (var1,var2))
'''
'''
L = ["one","for","all"]
print(L[1].split())
'''

x = int(input("Enter a number: "))
try:
    y = float(input("Enter a number: "))
except IOError:
    print ("IO Error")
except ValueError:
    print("Invalid Value")
print ("end")

