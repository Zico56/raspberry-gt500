import logging
import configparser

config = ''
testMode = 'False'

def main():
    logging.info("Loading configuration file")
    global config
    config = configparser.RawConfigParser()
    config.read('config.properties')
    
    global testMode
    testMode = config.getboolean('TESTING', 'gpio.emulator')

main()