# CSC 110 - Assignment #2
# Pharaoh's Friend Construction!
# Section 03
# Justin Clark
# 1/15/2020


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
            'ground area covered = {:,} {}'.format(groundAreaCovered, displayMetersSquared) + '\n' + \
            'pyramid volume = {:,.0f} {}'.format(pyramidVolume, displayMetersCubed) + '\n' + \
            'blocks = {:,}'.format(countOfBlocks) + '\n' + \
            'mass = {:,} kg'.format(mass)

        return displayAnswer


# input
pyramidSideLength = int(input('Input a side length (in meters) for a pyramid: '))
pyramidHeight = int(input('Input a height (in meters) for a pyramid: '))

# build instance of Pyramid
pyramid_1 = Pyramid(pyramidSideLength, pyramidHeight)
# display results of instance
print(Pyramid.createNewPyramid(pyramid_1))


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
