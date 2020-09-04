# TreeTest3.py
# This sample program demonstrates drawing shapes
# on a canvas using some Gui tools.
#
# Study the program GuiTest3.py before working with this program.
# Separate documents posted on the class web site describe how this
# sample program works and how do design your own scene elements.
#
# This program is not interactive.  It draws the same
# picture every time it is executed.
#
# To run this program, you must save the file Gui3.py
# in the same folder as this program.
#
# CSC 110
# W'18 (Python 3 version)

# Required import statement for Gui tools
import Gui3

# Named Constants 
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480

# Function Definition Section

# Draws one tree.  The parmeters base_x and base_y specify
# the location of a point at the center of the bottom edge
# of the tree trunk.  The last parameter is the height of
# the tree.  All parameters have units of pixels.
def draw_simple_tree(base_x, base_y, height):
    # draw trunk
    trunk_x1 = base_x - height * 0.05
    trunk_x2 = base_x + height * 0.05
    trunk_y1 = base_y
    trunk_y2 = base_y + height * 0.5
    canvas.rectangle([[trunk_x1, trunk_y1], [trunk_x2, trunk_y2]], \
                     fill='brown', width = 0)
    # draw crown
    # the polygon has 3 points, peak, lower left (LL), and lower right (LR)
    LL_x = base_x - height * 0.2
    LR_x = base_x + height * 0.2
    L_y = base_y + height * 0.3
    canvas.polygon([[base_x, base_y + height], [LL_x, L_y], [LR_x, L_y]], \
                   fill='darkgreen', width=0)

# Draws a cluster of three trees.  The parmeters x and y specify
# the location of a point at the center of the bottom edge
# of the tree trunk of the largest tree in the cluster.
# The last parameter is the "size" of the cluster -- the distance
# in pixels from the bottom to the top of the cluster.
def draw_tree_cluster(x, y, size):
    draw_simple_tree(x - size * 0.15, y + size * 0.5, size * 0.5)
    draw_simple_tree(x - size * 0.3, y + size * 0.3, size * 0.6)
    draw_simple_tree(x, y, size * 0.8)

def main():
    # draw things on the canvas
    draw_tree_cluster(0, 0, 50)
    draw_tree_cluster(-40, -30, 65)
    draw_tree_cluster(60, -120 , 120)
    draw_simple_tree(-80, -150, 140)
    draw_simple_tree(-100, -180, 160)

#####################################################################
#
# DO NOT CHANGE ANYTHING BELOW THIS LINE
#
#####################################################################

# Setup the canvas -- canvas is the drawing area
# Note that 'win' and 'canvas' are GLOBAL VARIABLES in this program
win = Gui3.Gui()
win.title('Playing around with Gui')
canvas = win.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# run the main function
main()

# show the window
win.mainloop()

# Here are some colors you can use: 'white', 'gray', 'black', 'red',
# 'green', 'blue', 'cyan', 'yellow', 'magenta', 'brown', 'darkgreen'
# Hundreds of colors here: https://wiki.tcl.tk/37701
# Official color documentation here:
# https://www.tcl.tk/man/tcl8.5/TkCmd/colors.htm
