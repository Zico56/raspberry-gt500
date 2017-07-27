import threading

class CustomThread(threading.Thread):
    def __init__(self, function):
        super().__init__()
        self.event = threading.Event()
        self.function = function

    def run(self):  
        while not self.event.is_set():
            self.function()