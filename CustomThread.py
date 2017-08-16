import threading
import logging

class CustomThread(threading.Thread):
    def __init__(self, function):
        super().__init__()
        self.event = threading.Event()
        self.function = function

    def run(self): 
        logging.info("Custom thread start") 
        try:
            while not self.event.is_set():
                self.function()
        except Exception as ex:
            print("Error in thread: " + dir(ex))
        finally:
            logging.info("Custom thread end") 