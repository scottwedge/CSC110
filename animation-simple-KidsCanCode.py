from tkinter import *

# https://www.youtube.com/watch?v=lc8NNJgeVjI time=3:54

import random
import time

tk = Tk()
canvas = Canvas(tk, width=1800, height=400)
tk.title("Simple Tkinter Animations")
canvas.pack()

ball = canvas.create_oval(10,10,60,60,fill='orange')

for i in range(1600):
    canvas.move(ball, 1, 0)
    time.sleep(0.01)
    tk.update()

tk.mainloop()