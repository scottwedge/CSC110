import signal

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

signal.signal(signal.SIGINT, signal_handler)

x = 0

interrupted = False
while True:
    x = x + 1
    print(x)

    if interrupted:
        print("Gotta go")
        break