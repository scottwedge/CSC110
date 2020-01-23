from tkinter import *
import math

# https://www.youtube.com/watch?v=r5EQCSW_rLQ  pyramid math formulas TIME=3:55

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

def clickFunction():

    pyramid_base = widthText.get()
    pyramid_height = heightText.get()

    responseText = 'Width entered: {}'.format(pyramid_base) + '\n' + \
        'Height entered: {}'.format(pyramid_height)

    responseLabel = Label(root, text=responseText)
    responseLabel.grid(row=3, column=0)

    createPyramid(pyramid_base, pyramid_height)

def createPyramid(pyramid_base, pyramid_height):
    canvas_width = 400
    canvas_height = 400

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.grid(row=5)
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

root = Tk()

root.title('Pyramid Dimensions')
root.geometry("500x600+1100+200")



widthLabel = Label(root, text="Enter Width:")
widthLabel.grid(row=0, column=0)

widthText = Entry(root)
widthText.grid(row=0, column=1)



heightLabel = Label(root, text="Enter Height:")
heightLabel.grid(row=1, column=0)

heightText = Entry(root)
heightText.grid(row=1, column=1)



submitButton = Button(root, text="Submit", command=clickFunction)
submitButton.grid(row=2, column=0)

closeButton = Button(master=root, text='Close', command=root.destroy)
closeButton.grid(row=2, column=1)

#==================================
# clickFunction() # REMOVE WHEN DONE
#==================================

root.mainloop()
