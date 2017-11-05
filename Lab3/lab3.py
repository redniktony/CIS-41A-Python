#@Author Xia Hua
#@Assigment 2 Due Oct 8

from ezgraphics import GraphicsWindow
from ezgraphics import GraphicsImage
from math import sqrt
import os
'''
Use the os dir in order to save files at same folder
'''
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
'''
Constructors
'''
picture = GraphicsImage(os.path.join(__location__, 'queen-mary.gif'))#Change if you want another pic
#check size
if(picture.height() > picture.width()):
    WIDTH=picture.height()
    HEIGHT=picture.width()
else:
    HEIGHT = picture.height()
    WIDTH = picture.width()
#Find middle point
HeightRow = HEIGHT//2
WidthCol = WIDTH//2
newimage = GraphicsImage(WIDTH,HEIGHT)

#For future use
#To do : make a square pic

'''
Main function
'''

print("Processing Images....Please Wait...")
#Find pixel
for row in range (HEIGHT):
    for col in range (WIDTH):
        if sqrt((row-HeightRow)**2+(col-WidthCol)**2) <= HEIGHT//2 :
            red = round(picture.getRed(row,col)*0.2126)
            green = round(picture.getGreen(row,col)*0.07152)
            blue = round(picture.getGreen(row,col)*0.0722)
            gray = red + green + blue
            newimage.setPixel(row,col,gray,gray,gray)
        else :
            newimage.setPixel(row,col,255,255,255)
newimage.save(os.path.join(__location__, 'queen-mary_lab3.gif'))#Change if you want another pic
print("Done")
print("Output image has been put into same folder name:'queen-mary_lab3.gif'")




