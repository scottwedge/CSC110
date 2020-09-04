from tkinter import *


# https://stackoverflow.com/questions/11502879/simple-animation-using-tkinter/11505034#11505034
# 

# ??? "import tkinter" VS "from tkinter import *" ???

# class for simulation data
# --------------------------------

class Visualization:

    # # __init__ is Python's constructor method
    # def __init__(self, pyramidSideLength, pyramidHeight):
    #     self.pyramidSideLength = pyramidSideLength
    #     self.pyramidHeight = pyramidHeight

    def __init__(self, s, canvasWidth, canvasHeight):
        # sets up the object
        self.s = s
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight

    def draw_one_frame(self, *args):
        canvas.create_oval([300,100], [325, 125], fill='green')

    def after(self, *args):
        canvas.create_oval([300+20,100+20], [325, 125], fill='green')

    def update_canvas(self, Event):
        pass
        # draws the next frame

        # canvas.delete(ALL)

        # draw some stuff
        # canvas.create_........

    # def move(self, item, dx, dy, transform=False):
    #     if transform:
    #         coords = [[0,0], [dx,dy]]
    #         p1, p2 = self.trans(coords)
    #         dx = p2.x - p1.x
    #         dy = p2.y - p1.y
    #     Canvas.move(self, item, dx, dy)

    # def circle(self, coord, r, fill='', **options):
    #     """make a circle with center at (x, y) and radius (r)
    #     """
    #     x, y = coord
    #     coords = self.trans([[x-r, y-r], [x+r, y+r]])
    #     tag = self.create_oval(coords, options, fill=fill)
    #     return Item(self, tag)


    def animate(self):
        self.draw_one_frame()
        self.after(100, self.animate)

    """
        Once you call this function once, it will continue 
        to draw frames at a rate of ten per second -- once 
        every 100 milliseconds. You can modify the code to 
        check for a flag if you want to be able to stop the 
        animation once it has started. For example:
    """

    # def animate(self):
    #     if not self.should_stop:
    #         self.draw_one_frame()
    #         self.after(100, self.animate)


# gui section
# ---------------------------------------

# initialise the Visualization object
s = 'something, but what?'
canvasWidth = 600
canvasHeight = 400
vis = Visualization(s, canvasWidth, canvasHeight)

# Tkinter init
root = Tk()

canvas = Canvas(root, width = canvasWidth, height = canvasHeight)

redBall = canvas.create_oval([100,100], [75, 75], fill='red')
yellowBall = canvas.create_oval([200,300], [225, 325], fill='yellow')

# set mouse click to advance the simulation
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind('<Button-1>', vis.update_canvas)

# run the main loop
root.mainloop()
