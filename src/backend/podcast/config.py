import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read(__package__ + '.conf')
