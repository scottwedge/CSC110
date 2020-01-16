# CSC 110 - Assignment #2
# Pharaoh's Friend Construction!
# Section 03
# Justin Clark
# 1/15/2020

# contants
BLOCK_HEIGHT = 1.5 # meters
BLOCK_WIDTH = 2 # meters
BLOCK_LENGTH = 2.5 # meters
BLOCK_WEIGHT = 15000 # kg

# input
pyramidSideLength = int(input('Input a side length for a pyramid: ')) # in meters
pyramidHeight = int(input('Input a height for a pyramid: ')) # in meters

# processing
def calculateBlockVolume(height, width, length):
    return height * width * length

def calculateGroundArea(length):
    return length ** 2

def calculatePyramidVolume(groundArea, height):
    return round((groundArea / 3) * height)

def countBlocks(pyramidVolume, blockVolume):
    return round(pyramidVolume / blockVolume)

def calculateMass(blocks, weight):
    return blocks * weight

# storing function output in variables for program readability
blockVolume = calculateBlockVolume(BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_LENGTH)
groundAreaCovered = calculateGroundArea(pyramidSideLength)
pyramidVolume = calculatePyramidVolume(groundAreaCovered, pyramidHeight)
countOfBlocks = countBlocks(pyramidVolume, blockVolume)
mass = calculateMass(countOfBlocks, BLOCK_WEIGHT)

# create superscript for displaying exponents
superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
displayMetersSquared = 'm2'.translate(superscript)
displayMetersCubed = 'm3'.translate(superscript)


displayAnswer = '\n' + \
    'ground area covered = {:,} {}'.format(groundAreaCovered, displayMetersSquared) + '\n' + \
    'pyramid volume = {:,.0f} {}'.format(pyramidVolume, displayMetersCubed) + '\n' + \
    'blocks = {:,}'.format(countOfBlocks) + '\n' + \
    'mass = {:,} kg'.format(mass)

print(displayAnswer)

# automated tests
print('\nrunning automated tests...')
import unittest

class TestThisProgram(unittest.TestCase):
    
    def test_calculateBlockVolume(self):
        # only one test for block size (not supposed to change)
        self.assertEqual(calculateBlockVolume(1.5, 2, 2.5), 7.5)

    def test_calculateGroundArea(self):
        self.assertEqual(calculateGroundArea(80), 6400)
        self.assertEqual(calculateGroundArea(236), 55696)

    def test_calculatePyramidVolume(self):
        self.assertEqual(calculatePyramidVolume(6400, 64), 136533)
        self.assertEqual(calculatePyramidVolume(55696, 138), 2562016)
        
    def test_countBlocks(self):
        self.assertEqual(countBlocks(136533, 7.5), 18204)
        self.assertEqual(countBlocks(2562016, 7.5), 341602)

    def test_calculateMass(self):
        self.assertEqual(calculateMass(18204, 15000), 273060000)
        self.assertEqual(calculateMass(341602, 15000), 5124030000)

if __name__ == '__main__':
    unittest.main()

# ===================================
# manual tests:
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
#   pyramid side length = 80 meters; 
#   pyramid height = 64 meters
# ========
# results:
#   ground area covered = 55,696 m²
#   pyramid volume = 2,562,016 m³
#   blocks = 341,602
#   mass = 5,124,030,000 kg
# ===================================
