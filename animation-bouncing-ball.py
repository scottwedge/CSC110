import signal
import sys
import Gui
import threading
import time

win = Gui.Gui()
win.title('Bouncing Ball')
canvas = win.ca(width = 640, height = 480)
ball = canvas.circle([0,0], 25, fill='magenta')




def signal_handler(signal, frame):
    global interrupted
    interrupted = True
    time.sleep(5)
    print('close window signal detected')

signal.signal(signal.SIGINT, signal_handler)

def _delete_window():
    # global interrupted
    
    print ("delete_window")
    try:
        # interrupted = True
        win.quit()
        win.destroy()
    except:
        pass

def _destroy(event):
    print ("destroy")

win.protocol("WM_DELETE_WINDOW", _delete_window)
win.bind("<Destroy>", _destroy)

win.bu(text='Destroy', command=win.destroy)

def main():


        
    # def signal_handler(signal, frame):
    #     global interrupted
    #     interrupted = True

    def playBall():

        dx = .01
        yx = .01

        interrupted = False
        while True:

            ball.move(dx,yx)

            currentCoordinates = canvas.coords(ball)
            x1 = currentCoordinates[0]
            y1 = currentCoordinates[1]
            x2 = currentCoordinates[2]
            y2 = currentCoordinates[3]

            if x1 < 0:
                yx = yx * 1
                dx = dx * -1
                ball.move(dx, yx)
            if y1 < 0:
                yx = yx * -1
                dx = dx * 1
                ball.move(dx, yx)
            if x2 > 640:
                yx = yx * 1
                dx = dx * -1
                ball.move(dx, yx)
            if y2 > 480:
                yx = yx * -1
                dx = dx * 1
                ball.move(dx, yx)   

            if interrupted:
                print("Gotta go")
                break
            win.update()

    timer = threading.Timer(.2, playBall) 
    timer.start()

main()

win.mainloop()
