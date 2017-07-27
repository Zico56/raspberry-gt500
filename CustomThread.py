import threading
import time

SDI = 17
RCLK = 18
SRCLK = 27

def getlist(option, sep=','):
    return [ int(chunk,16) for chunk in option.split(sep) ]

class CustomThread(threading.Thread):
    def __init__(self, function):
        super().__init__()
        self.event = threading.Event()
        self.function = function

    def run(self):  
        while not self.event.is_set():
            self.function()