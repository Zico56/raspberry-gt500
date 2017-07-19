import logging
import configparser

config = ''

def main():
    logging.info("Loading configuration file")
    global config
    config = configparser.RawConfigParser()
    config.read('config.properties')

main()