import logging
import configparser

####### CONFIG #######
config = configparser.RawConfigParser()
config.read('config.properties')

####### LOGGER #######
logLevel = config.get('LOGGING', 'log.level')
logFile = config.get('LOGGING', 'log.file')
logging.basicConfig(format='%(asctime)s : %(message)s', datefmt='%d/%m/%Y %H:%M:%S', filename=logFile, level=logLevel)
logger = logging.getLogger('Application')

def log():
    logger.info("test")