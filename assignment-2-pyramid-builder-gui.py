from tkinter import *
import math

# https://stackoverflow.com/questions/54637795/how-to-make-a-tkinter-canvas-rectangle-transparent 

# https://www.youtube.com/watch?v=r5EQCSW_rLQ  pyramid math formulas TIME=3:55

class GridLines:
    
    def __init__(self, canvas, canvas_width, canvas_height, grid_space):
        self.canvas = canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.grid_space = grid_space

    def __vertical_lines__(self):
        for i in range(0, self.canvas_height, self.grid_space):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='pink')

    def __horizontal_lines__(self):
        for i in range(0, self.canvas_width, self.grid_space):
            self.canvas.create_line(0, i, self.canvas_width, i, fill='cyan')

    def create_grid(self):
        self.__vertical_lines__()
        self.__horizontal_lines__()

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

def clickFunction():

    # width = widthText.get()
    # height = heightText.get()
    width = 80
    height = 64

    responseText = 'Width entered: {}'.format(width) + '\n' + \
        'Height entered: {}'.format(height)

    responseLabel = Label(root, text=responseText)
    responseLabel.grid(row=3, column=0)

    createPyramid(width, height)


submitButton = Button(root, text="Submit", command=clickFunction)
submitButton.grid(row=2, column=0)

closeButton = Button(master=root, text='Close', command=root.destroy)
closeButton.grid(row=2, column=1)

print('GUI created and displayed')

def createPyramid(width, height):
    canvas_width = 400
    canvas_height = 400

    canvas = Canvas(root, width=canvas_width, height=canvas_height)
    canvas.grid(row=5)
    canvas.configure(background='white')

    grid = GridLines(canvas, canvas_width, canvas_height, 20)
    GridLines.create_grid(grid)

    points = [[100,300],[300,300], [200, 100]]
    canvas.create_polygon(points, outline='black', fill='')


    points2 = [[100,300],[200,100],[160,220]]
    canvas.create_polygon(points2, outline='black', fill='gray')

    # canvas.create_line(200, 100, 160, 220, fill='magenta') # back-left
    # canvas.create_line(160, 220, 100, 300, fill='magenta') # left-connector

    canvas.create_line(200, 100, 160, 220, fill='magenta') # back-left
    canvas.create_line(320, 220, 160, 220, fill='blue') # back-middle
    canvas.create_line(320, 220, 200, 100, fill='green') # back-right

    canvas.create_line(160, 220, 100, 300, fill='magenta') # left-connector
    canvas.create_line(320, 220, 300, 300, fill='blue') # right-connector

    canvas.create_oval([200-(50/2),100-50], [225-(50/2), 125-50]) # sun

# ===========================
clickFunction() # REMOVE
# ===============================

root.mainloop()
# https://www.youtube.com/watch?v=YXPyB4XeYLA  minute 25?
