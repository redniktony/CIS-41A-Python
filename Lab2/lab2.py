from ezgraphics import * #GraphicsWindow

#Qustion 1

timein=int(input("Please enter the start time: ")) 
timeout=int(input("Please enter the end time: "))
hours1=timein//100
mins1=timein%100
hours2=timeout//100
mins2=timeout%100
print( hours2-hours1,"hours",mins2-mins1,"minutes")

#Question 2
from ezgraphics import *
#Constructor 
win = GraphicsWindow(640, 480)
origionalX = 100
origionalY = 100
#First circle
canvas = win.canvas()
canvas.setOutline("blue")
canvas.setLineWidth(5)
canvas.drawOval(origionalX,origionalY,100,100)
#Second circle
canvas.setOutline("black")
canvas.setLineWidth(5)
canvas.drawOval(origionalX+100,origionalY,100,100)
#Third circle
canvas.setOutline("red")
canvas.setLineWidth(5)
canvas.drawOval(origionalX+200,origionalY,100,100)
#Fourth circle
canvas.setOutline("yellow") 
canvas.setLineWidth(5)
canvas.drawOval(origionalX+45,origionalY+60,100,100)
#Fifth circle
canvas.setOutline("green")
canvas.setLineWidth(5)
canvas.drawOval(origionalX+145,origionalY+60,100,100)
#Print text
canvas.setOutline("red")
canvas.drawText(200,300,"The Olympic rings")
win.wait()  
