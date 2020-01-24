from tkinter import *
# import math

# https://www.youtube.com/watch?v=r5EQCSW_rLQ  pyramid math formulas TIME=3:55

class Pyramid:

    # contants
    BLOCK_HEIGHT = 1.5 # meters
    BLOCK_WIDTH = 2 # meters
    BLOCK_LENGTH = 2.5 # meters
    BLOCK_WEIGHT = 15000 # kg

    # __init__ is Python's constructor method
    def __init__(self, pyramidSideLength, pyramidHeight):
        self.pyramidSideLength = pyramidSideLength
        self.pyramidHeight = pyramidHeight

    # processing
    def calculateBlockVolume(self, height, width, length):
        return height * width * length

    def calculateGroundArea(self, length):
        return length ** 2

    def calculatePyramidVolume(self, groundArea, height):
        return round((groundArea / 3) * height)

    def countBlocks(self, pyramidVolume, blockVolume):
        return round(pyramidVolume / blockVolume)

    def calculateMass(self, blocks, weight):
        return blocks * weight

    # this type of function might not be suitable for inside a class, but going with it for now
    def createNewPyramid(self):
        # create superscript for displaying exponents
        superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        displayMetersSquared = 'm2'.translate(superscript)
        displayMetersCubed = 'm3'.translate(superscript)

        # storing function output in variables for program readability
        blockVolume = self.calculateBlockVolume(Pyramid.BLOCK_HEIGHT, Pyramid.BLOCK_WIDTH, Pyramid.BLOCK_LENGTH)
        groundAreaCovered = self.calculateGroundArea(self.pyramidSideLength)
        pyramidVolume = self.calculatePyramidVolume(groundAreaCovered, self.pyramidHeight)
        countOfBlocks = self.countBlocks(pyramidVolume, blockVolume)
        mass = self.calculateMass(countOfBlocks, Pyramid.BLOCK_WEIGHT)

        # build nicely formatted answer for display
        displayAnswer = '\n' + \
            'Ground Area Covered = {:,} {}'.format(groundAreaCovered, displayMetersSquared) + '\n' + \
            'Pyramid Volume = {:,.0f} {}'.format(pyramidVolume, displayMetersCubed) + '\n' + \
            'Blocks = {:,}'.format(countOfBlocks) + '\n' + \
            'Mass = {:,} kg'.format(mass) + '\n\n' + \
            '*Pyramid is not to scale.'

        return displayAnswer

class GridLines:
    
    def __init__(self, canvas, canvas_width, canvas_height, grid_space):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.grid_space = grid_space

    def __vertical_lines__(self):
        for i in range(0, self.canvas_height, self.grid_space):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='thistle1')

    def __horizontal_lines__(self):
        for i in range(0, self.canvas_width, self.grid_space):
            self.canvas.create_line(0, i, self.canvas_width, i, fill='CadetBlue1')

    def create_grid(self):
        self.__vertical_lines__()
        self.__horizontal_lines__()

def createPyramid(pyramid_base, pyramid_height):

    canvas_width = 400
    canvas_height = 400

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.grid(row=5, column=0, columnspan=2, sticky=E)
    canvas.configure(background='white')

    grid = GridLines(canvas, canvas_width, canvas_height, 20)
    GridLines.create_grid(grid)

    # y-coords
    y_top = pyramid_height #y_top = 100
    y_middle = 220
    y_bottom = pyramid_base #y_bottom = 300

    # x-coords
    x_center = 200
    x_front_left = 100
    x_back_left = 160
    x_back_right = 320
    x_front_right = 300

    # front triangle
    points = [[x_front_left,y_bottom], [x_front_right,y_bottom], [x_center, y_top]]
    canvas.create_polygon(points, outline='black', fill='')

    # left side triangle
    points2 = [[x_front_left,y_bottom], [x_center,y_top], [x_back_left,y_middle]]
    canvas.create_polygon(points2, outline='black', fill='')

    # right side triangle
    points3 = [[x_center,y_top], [x_back_right,y_middle], [x_front_right,y_bottom]]
    canvas.create_polygon(points3, outline='black', fill='gray90')

    # triangle lines
    canvas.create_line(x_center, y_top, x_back_left, y_middle, fill='magenta') # back-left
    canvas.create_line(x_back_right, y_middle, x_back_left, y_middle, fill='magenta') # back-middle
    canvas.create_line(x_back_right, y_middle, x_center, y_top, fill='magenta') # back-right
    canvas.create_line(x_back_left, y_middle, x_front_left, y_bottom, fill='blue') # left-connector
    canvas.create_line(x_back_right, y_middle, x_front_right, y_bottom, fill='blue') # right-connector

    # canvas.create_oval([x_center-30,y_top-60], [x_center+30,y_top], fill='LightYellow') # sun

def clickFunction():

    pyramid_base = int(widthText.get())
    pyramid_height = int(heightText.get())
    
    # build instance of Pyramid
    new_pyramid = Pyramid(pyramid_base, pyramid_height)

    # display results of instance (outputs calculated data)
    pyramid_dimensions_output = Pyramid.createNewPyramid(new_pyramid)
    responseLabel = Label(root, text=pyramid_dimensions_output, justify=LEFT)
    responseLabel.grid(row=4, column=0, columnspan=2, ipadx='110', sticky=W)

    # outputs 3D graphic of pyramid (not to scale)
    createPyramid(pyramid_base, pyramid_height)
    
root = Tk()

root.title('Pyramid Dimensions')
root.geometry("600x700+1100+200")

header = Label(root, text='Pyramid Builder', font='Helvetica 18 bold')
header.grid(row=0, column=0, columnspan=2, pady='10')

# width entry
widthLabel = Label(root, text="Enter Base (in meters):")
widthLabel.grid(row=1, column=0, ipadx='30', sticky=W)
widthText = Entry(root)
widthText.grid(row=1, column=1, ipadx="100")
widthText.focus()

# height entry
heightLabel = Label(root, text="Enter Height (in meters):")
heightLabel.grid(row=2, column=0, ipadx='30', sticky=W)
heightText = Entry(root)
heightText.grid(row=2, column=1, ipadx="100")

# buttons
buttonFrame = Frame(root)
buttonFrame.grid(row=3, column=1, sticky=E)

submitButton = Button(buttonFrame, text="Submit", command=clickFunction)
closeButton = Button(buttonFrame, text='Close', command=root.destroy)

submitButton.pack(side='left', padx='2')
closeButton.pack(side='left', padx='2')

# root.grid_columnconfigure(0, minsize=80)
# root.grid_rowconfigure(0, pad=5)

root.mainloop()

# automated tests (would normally be in separate file just for testing)
print('\nrunning automated tests...')

import unittest
# would use "import Pyramid" here if in separate file

class TestPyramid(unittest.TestCase):
    # "self" is not normally required in: ClassName.methodCall(self), but needed because class is in same file as unit test
    
    def test_calculateBlockVolume(self):
        # only one test for block size (not supposed to change)
        self.assertEqual(Pyramid.calculateBlockVolume(self, 1.5, 2, 2.5), 7.5)

    def test_calculateGroundArea(self):
        self.assertEqual(Pyramid.calculateGroundArea(self, 80), 6400)
        self.assertEqual(Pyramid.calculateGroundArea(self, 236), 55696)

    def test_calculatePyramidVolume(self):
        self.assertEqual(Pyramid.calculatePyramidVolume(self, 6400, 64), 136533)
        self.assertEqual(Pyramid.calculatePyramidVolume(self, 55696, 138), 2562016)
        
    def test_countBlocks(self):
        self.assertEqual(Pyramid.countBlocks(self, 136533, 7.5), 18204)
        self.assertEqual(Pyramid.countBlocks(self, 2562016, 7.5), 341602)

    def test_calculateMass(self):
        self.assertEqual(Pyramid.calculateMass(self, 18204, 15000), 273060000)
        self.assertEqual(Pyramid.calculateMass(self, 341602, 15000), 5124030000)

# Runs the unit tests automatically in the current file
if __name__ == '__main__':
    unittest.main()

# ===========================================
# Visual of correct output for 2 test cases:
# results agree with automated unit testing
# and hand calculations (in MS Excel).
# ===================================
# input data: 
#   pyramid side length = 80 meters; 
#   pyramid height = 64 meters
# ========
# results: 
#   ground area covered = 6,400 m²
#   pyramid volume = 136,533 m³
#   blocks = 18,204
#   mass = 273,060,000 kg
# ===================================
# input data: 
#   pyramid side length = 236 meters; 
#   pyramid height = 138 meters
# ========
# results:
#   ground area covered = 55,696 m²
#   pyramid volume = 2,562,016 m³
#   blocks = 341,602
#   mass = 5,124,030,000 kg
# ===========================================
