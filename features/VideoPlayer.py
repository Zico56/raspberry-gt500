import logging
from subprocess import Popen
from Configuration import config
from Configuration import testMode
from features.GenericFeature import *

class VideoPlayer(GenericFeature):

    # Path to video to play
    path = config.get('VIDEO', 'PATH')

    def __init__(self, parent, configSection):
        super().__init__(parent, configSection)

    def start(self):
        logging.info("Video player start")
        if not testMode:
            omxc = Popen(['omxplayer', '-b', self.path])
             
    def stop(self):
        logging.info("Video player stop")
        if not testMode:
            os.system('killall omxplayer.bin')
