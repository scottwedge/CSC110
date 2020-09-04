import Gui
win = Gui.Gui()

canvas = win.ca(width = 640, height = 480)

canvas.circle([0,0], 25, fill='magenta')

win.mainloop()