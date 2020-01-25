from tkinter import *
import math

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

# def createPyramid(pyramid_center, pyramid_base, pyramid_height):
#     """creates 3d graphic of pyramid.
#         takes base and height of pyramid as arguments"""

#     # x-coords
#     x_center = pyramid_center
#     x_front_left = x_center / 2
#     x_back_left = x_center / 1.25
#     x_back_right = x_center * 1.6               #right_offset = ((base * 1.1) - base)

#     x_front_right = 200 * 1.5

#     # y-coords
#     y_top = pyramid_height #y_top = 100
#     y_middle = x_center * 1.1                   # height * .6
#     y_bottom = pyramid_base #y_bottom = 300

#     # front triangle
#     points = [[x_front_left,y_bottom], [x_front_right,y_bottom], [x_center, y_top]]
#     canvas.create_polygon(points, outline='black', fill='')

#     # right side triangle
#     points3 = [[x_center,y_top], [x_back_right,y_middle], [x_front_right,y_bottom]]
#     canvas.create_polygon(points3, outline='black', fill='gray90')

#     # triangle lines
#     canvas.create_line(x_center, y_top, x_back_left, y_middle, fill='magenta', dash=(4,4)) # back-left
#     canvas.create_line(x_back_right, y_middle, x_back_left, y_middle, fill='magenta', dash=(4,4)) # back-middle
#     canvas.create_line(x_back_left, y_middle, x_front_left, y_bottom, fill='blue', dash=(4,4)) # left-connector
#     canvas.create_line(x_back_right, y_middle, x_front_right, y_bottom, fill='blue') # right-connector

def createTriangle(apex, base, height):

    x_center = apex[0]
    y_top = apex[1]

    y_bottom = y_top + height
    y_middle = y_top + height / 1.6

    half_base = base / 2
    x_left = x_center - (half_base)
    x_right = x_center + (half_base)

    right_offset = ((base * 1.1) - base)
    x_right_rear = x_right + right_offset

    left_offset = ((base * .6) - half_base)
    x_left_rear = x_center - left_offset
    
    # facing triangle
    points = [[x_left,y_bottom], [x_right,y_bottom], apex]
    canvas.create_polygon(points, outline='black', fill='gray95')

    # right side shadow
    points3 = [apex, [x_right_rear,y_middle], [x_right,y_bottom]]
    canvas.create_polygon(points3, outline='black', fill='gray80')

    # triangle lines
    canvas.create_line(x_center, y_top, x_left_rear, y_middle, fill='thistle3', dash=(4,4)) # back-left
    canvas.create_line(x_right_rear, y_middle, x_left_rear, y_middle, fill='CadetBlue3', dash=(4,4)) # back-middle
    canvas.create_line(x_right_rear, y_middle, x_left, y_bottom, fill='PaleGreen3', dash=(4,4)) # cross positive
    canvas.create_line(x_left_rear, y_middle, x_left, y_bottom, fill='CadetBlue3', dash=(4,4)) # left connector
    canvas.create_line(x_left_rear, y_middle, x_right, y_bottom, fill='PaleGreen3', dash=(4,4)) # cross negative

def clickFunction():

    createTriangle([100,100], 200, 120)
    createTriangle([200,200], 100, 120)
    createTriangle([300,300], 100, 120)

    # pyramid_base = int(widthText.get())
    # pyramid_height = int(heightText.get())

    # pyramid_center = 200
    # pyramid_base = 300
    # pyramid_height = 100

    # outputs 3D graphic of pyramid (not to scale)
    # createPyramid(pyramid_center, pyramid_base, pyramid_height)


root = Tk()

root.iconbitmap('pyramid.ico')
root.title('Pyramid Sce')
root.geometry("600x700+1100+200")

# =========================================

canvas_width = 400
canvas_height = 400

canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=4, column=0, columnspan=2, sticky=E)
canvas.configure(background='white')

grid = GridLines(canvas, canvas_width, canvas_height, 20)
GridLines.create_grid(grid)

# =========================================


# from PIL import ImageTk, Image
# import os
# img = ImageTk.PhotoImage(Image.open("pyramid.png"))
# panel = Label(root, image = img)
# panel.pack(side = "bottom", fill = "both", expand = "yes")

# image_frame = Frame(root)
# image_frame.grid(row=0, column=0, sticky=W)

# image create photo imgobj -file "pyramid.png" -width 400 -height 400 
# pack [label .myLabel].myLabel configure -image imgobj 





# widthLabel = Label(root, image='pyramid.png')
# widthLabel.grid(row=0, column=0, ipadx='30', sticky=W)

header = Label(root, text='Pyramid Scene Builder', font='Helvetica 18 bold')
header.grid(row=0, column=1, columnspan=2, pady='10')

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



# =========================================
clickFunction()
# =========================================

root.mainloop()