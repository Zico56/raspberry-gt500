import logging
import time
from features.GenericFeature import *

class StopFeature(GenericFeature):

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def processEvent(self, event):
        self.parent.winfo_toplevel().destroy()
