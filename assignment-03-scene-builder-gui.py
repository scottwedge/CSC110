from tkinter import *
import math

def createSky():
    canvas.create_rectangle(0,0,440,220,fill='SkyBlue2')

def createCelestialObject(xCoord, yCoord, diameter, color, border):
    canvas.create_oval(xCoord, yCoord, xCoord+diameter, yCoord+diameter, fill=color, outline=border)

def createCloud(xCoord, yCoord, diameter, shade):
    canvas.create_oval(xCoord, yCoord, xCoord+diameter, yCoord+diameter, fill=shade, outline='')
    canvas.create_oval(xCoord, yCoord+.5, xCoord+diameter, yCoord+diameter, fill=shade, outline='black')
    canvas.create_oval(xCoord, yCoord+2, xCoord+diameter, yCoord+diameter, fill=shade, outline='')

def createClouds(coords, shade):

    xCoord = coords[0]
    yCoord = coords[1]

    createCloud(xCoord+0,yCoord+20,80,shade)
    createCloud(xCoord+120,yCoord+40,80,shade)
    createCloud(xCoord+40,yCoord+0,120,shade)
    createCloud(xCoord+180,yCoord+60,40,shade)

    canvas.create_rectangle(xCoord+5,yCoord+80, xCoord+220,yCoord+120,fill='SkyBlue2')
    canvas.create_rectangle(xCoord+5,yCoord+80+.5, xCoord+220+1,yCoord+120+1,fill='SkyBlue2',outline='')

def createGround():
    canvas.create_rectangle(0,205,440,310,fill='goldenrod1')

def createPyramid(apex, base, height, facing_side, left_side):

    x_center = apex[0]
    y_top = apex[1]

    y_bottom = y_top + height
    y_middle = y_top + height / 1.02

    half_base = base / 2
    x_left = (x_center - (half_base))
    x_right = x_center + (half_base)
    
    left_offset = ((base * 1.1) - half_base)
    x_left_rear = x_center - left_offset
    
    # facing triangle
    points = [[x_left,y_bottom+4], [x_right,y_bottom], apex]
    canvas.create_polygon(points, outline='black', fill=facing_side)

    # left side shadow
    points3 = [apex, [x_left_rear,y_middle], [x_left,y_bottom+4]]
    canvas.create_polygon(points3, outline='black', fill=left_side)

def buildScene():

    createSky()
    
    createCelestialObject(-12, -12, 35, 'yellow2', 'black') # sun
    createCelestialObject(380, 110, 15, 'white', 'black') # moon
    createCelestialObject(384, 110, 15, 'SkyBlue2', 'black') # moon crescent outline
    createCelestialObject(385, 110, 15, 'SkyBlue2', '') # moon crescent shadow

    createClouds([10,20], 'white')

    createGround()

    createPyramid([360,120], 150, 100, 'goldenrod3', 'goldenrod1') # Great Pyramid of Khufu (right, [farthest])
    createPyramid([245,45], 280, 175+10, 'DarkGoldenrod2', 'goldenrod1') # Pyramid of Khafre (center)
    createPyramid([130,60], 260, 160+20, 'goldenrod2', 'goldenrod1') # Pyramid of Menkaure (left)

    createPyramid([205,140+5],120,80+20, 'goldenrod2', 'goldenrod1') # sm middle
    createPyramid([80,160+10],100,60+20, 'goldenrod2', 'goldenrod1') # sm left

    

# initialize tkinter
root = Tk()

# program constants
APP_NAME = 'Pyramids of Giza'

# create app window
root.iconbitmap('pyramid.ico')
root.title(APP_NAME)
root.geometry("600x500+1250+100")

# create scene header
header = Label(root, text=APP_NAME, font='Helvetica 18 bold')

# center the header
header.grid(row=0, column=0, sticky="EW", pady=60)
root.grid_columnconfigure(0, weight=1)

# create canvas
canvas = Canvas(root, width=430, height=300)

# center the canvas
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

# build scene
buildScene()

# infnite loop breaks only by interrupt 
root.mainloop()