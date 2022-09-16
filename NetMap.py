#Imports

from icmplib import multiping, ping
import configparser
import json
import sys

#Reading configuration files

config = configparser.ConfigParser()
config.read('network.ini')
sections = config.sections()

sourceOptions = config.options('SOURCE')
sourceItems = config.items('SOURCE')