import signal

def myHandler(signum,frame):
    print signum

signal.signal(signal.SIGTSTP,myHandler)

signal.pause()

print 'End'
