"""This program demonstrates building a somewhat complex scene."""

# CSC 110 - Assignment #3 -- Drawing a Scene -- Functional Decomposition!
# The Great Pyramids of Giza
# Section 03
# Justin Clark
# 1/24/2020

from tkinter import *
import math

# Inspiration for Scene:
#   Water Color Painting
#   https://medium.com/@arcaesthetics/monuments-in-watercolor-ep-02-pyramid-complex-at-giza-2faf1b5bf108
#   Real Photo
#   https://www.egypttoursplus.com/wp-content/uploads/2014/03/Best-Egypt-Vacations.jpg

def createSky():
    """creates a sky colored background
    """
    canvas.create_rectangle(0,0,440,220,fill=SKY_COLOR)

def createCelestialObject(xCoord, yCoord, diameter, color, border_color):
    """creates a celestial object at the given coordinates
    """
    canvas.create_oval(xCoord, yCoord, xCoord+diameter, yCoord+diameter, fill=color, outline=border_color)

def createCloudSection(xCoord, yCoord, diameter, shade):
    """creates subsections of cloud formation
    """

    # first oval creates shining effect at the top of the clouds
    canvas.create_oval(xCoord, yCoord, xCoord+diameter, yCoord+diameter, fill=shade, outline='')

    # this oval has a black outline which creates section shadow effects
    canvas.create_oval(xCoord, yCoord+.5, xCoord+diameter, yCoord+diameter, fill=shade, outline='black')

    # this oval has no outline and hides the rest of the black outline created above
    canvas.create_oval(xCoord, yCoord+2, xCoord+diameter, yCoord+diameter, fill=shade, outline='')

def createCloudObject(coords, shade, size):
    """creates cloud grouping
    """

    xCoord = coords[0]
    yCoord = coords[1]

    # y coordinate variables
    yc20 = 20 / size
    yc40 = 40 / size
    yc60 = 60 / size
    yc80 = 80 / size
    yc120 = 120 / size

    # x coordinate variables
    xc5 = 5 / size
    xc40 = 40 / size
    xc120 = 120 / size
    xc180 = 180 / size
    xc220 = 220 / size

    # diameter variables
    d40 = 40 / size
    d80 = 80 / size
    d120 = 120 / size

    # creates a cloud with four rounded sections of different sizes
    createCloudSection(xCoord+0,yCoord+yc20,d80,shade)
    createCloudSection(xCoord+xc120,yCoord+yc40,d80,shade)
    createCloudSection(xCoord+xc40,yCoord+0,d120,shade)
    createCloudSection(xCoord+xc180,yCoord+yc60,d40,shade)

    # adds a sky colored retangle with black boarder to create flat black outline for bottom of clouds
    canvas.create_rectangle(xCoord+xc5,yCoord+yc80, xCoord+xc220,yCoord+yc120,fill=SKY_COLOR)

    # adds a second sky colored retangle slightly wider and taller than the one above to hide it's other borders
    canvas.create_rectangle(xCoord+xc5,yCoord+yc80+.5, xCoord+xc220+1,yCoord+yc120+1,fill=SKY_COLOR ,outline='')

def createBirdWing(xCoord, yCoord, diameter, overlap, background_color):
    """creates one side of a flying bird
    """

    # this oval has a black outline which creates section shadow effects
    canvas.create_oval(xCoord, yCoord, xCoord+diameter, yCoord+diameter, fill='black', outline='black')

    # this oval has no outline and hides the rest of the black outline created above
    canvas.create_oval(xCoord, yCoord+overlap, xCoord+diameter, yCoord+diameter, fill=background_color, outline='')

def createBird(coords, diameter, overlap, background_color):
    """creates a bird flying in the sky
    """

    # get the x and y coords
    xCoord = coords[0]
    yCoord = coords[1]
    
    # creates left wing
    createBirdWing(xCoord, yCoord, diameter, overlap, background_color)

    # creates right wing
    createBirdWing(xCoord+diameter, yCoord, diameter, overlap, background_color)

def createGround():
    """creates a sand colored ground
    """
    canvas.create_rectangle(0,205,440,310,fill='goldenrod1')

def createPyramid(apex, base, height, facing_color, adjacent_color):
    """creates a 3d looking pyramid
    """

    # get x and y coords from apex
    x_center = apex[0]
    y_top = apex[1]

    # set the y coords for the front and back of the base
    y_bottom = y_top + height
    y_middle = y_top + height / 1.02

    # get set the left and right side purportions from center
    half_base = base / 2
    x_left = (x_center - (half_base))
    x_right = x_center + (half_base)
    
    # create an offset to give the illusion of 3 dimensions
    left_offset = ((base * 1.1) - half_base)
    x_left_rear = x_center - left_offset
    
    # facing triangle
    points = [[x_left,y_bottom+4], [x_right,y_bottom], apex]
    canvas.create_polygon(points, outline='black', fill=facing_color)

    # adjacent side triangle
    points3 = [apex, [x_left_rear,y_middle], [x_left,y_bottom+4]]
    canvas.create_polygon(points3, outline='black', fill=adjacent_color)

def buildScene():
    """this is the main function where we build the scene.
    """

    createSky()
    
    # clouds get smaller and darker as they get farther away
    createCloudObject([20,30], 'white', 1.5)
    createCloudObject([250,60], 'Gray90', 3)
    createCloudObject([320,90], 'Gray87', 5)
    createCloudObject([400,130], 'Gray85', 6)

    # birds flying in sky
    createBird([20,30], 10, 2, SKY_COLOR) # bird flying near sun
    createBird([60,50], 10, 2, 'white') # bird flying in front of big cloud
    createBird([275,73], 8, 1, 'Gray90') # bird flying in front of cloud near pyramid
    createBird([333,115], 6, .5, SKY_COLOR) # bird flying in front of smaller cloud

    # sun
    createCelestialObject(-12, -12, 35, 'yellow2', 'black')

    # creates "full" moon
    createCelestialObject(380, 110, 15, 'white', 'black') # full circle
    
    # create crescent moon by overlapping circles
    createCelestialObject(384, 110, 15, SKY_COLOR, 'black') # sky colored circle with black outline
    createCelestialObject(385, 110, 15, SKY_COLOR, '') # sky colored circle with no outline

    createGround()

    # major pyramids (from left, smallest to largest)
    createPyramid([360, 120], 150, 100, 'goldenrod3', 'goldenrod1') # Great Pyramid of Khufu (right)
    createPyramid([245, 45], 280, 185, 'DarkGoldenrod2', 'goldenrod1') # Pyramid of Khafre (center)
    createPyramid([130, 60], 260, 180, 'goldenrod2', 'goldenrod1') # Pyramid of Menkaure (left)

    # bird flying in front of pyramid
    createBird([240,67], 8, 1,'DarkGoldenrod2')
    
    # smaller pyramids up front
    createPyramid([205, 145], 120, 100, 'goldenrod2', 'goldenrod1') # sm middle
    createPyramid([80, 170], 100, 80, 'goldenrod2', 'goldenrod1') # sm left

# initialize tkinter
root = Tk()

# program constants
APP_NAME = 'The Great Pyramids of Giza'
SKY_COLOR = 'SkyBlue2'

# create app window
root.iconbitmap('pyramid.ico')
root.title(APP_NAME)
root.geometry("768x432+600+300")

# create scene header
header = Label(root, text=APP_NAME, font='Helvetica 18 bold')

# center the header
header.grid(row=0, column=0, sticky="EW", pady=20)
root.grid_columnconfigure(0, weight=1)

# create author/artist signature
header = Label(root, text='By Justin Clark', font='Times 10 italic')

# center signature
header.grid(row=1, column=0, sticky="EW", pady=300)
root.grid_columnconfigure(0, weight=1)

# create canvas
canvas = Canvas(root, width=430, height=300)

# center the canvas
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

# build scene
buildScene()

# infnite loop breaks only by interrupt 
root.mainloop()
