#Imports

from icmplib import multiping
import configparser
import json


# Reading configuration files

config = configparser.ConfigParser()
config.read('network.ini')
sections = config.sections()

sourceOptions = config.options('SOURCE')
sourceItems = config.items('SOURCE')

# Make lists for sources and targets
src_list = []
target_list = []

for i in range(len(sourceItems)):
    src_list.append(sourceItems[i][1])

targetOptions = config.options('TARGET')
targetItems = config.items('TARGET')

for i in range(len(targetItems)):
    target_list.append(targetItems[i][1])

targetsDict = {}  # Empty dictionary to store targets

# Not the most elegant solution, but it works

# the next bit of code just pings multiple targets and outputs TRUE or FALSE in a json
while True:
    for s in src_list:
        host = multiping(target_list, count=3, source=s)  # pings every target 3 times
        for h in range(len(host)):
            if s == src_list[0]:
                if host[h].is_alive:
                    targetsDict[target_list[h]] = "TRUE"
                else:
                    targetsDict[target_list[h]] = "FALSE"
        with open("targets.json", 'w') as output:
            output.write(json.dumps(targetsDict))

        # dump the json in a javascript file to import it in the webpage, another non-elegant solution, but it works
        with open("E:\\___REPOSITORIES\\NETSTAT\\html_template\\declare.js", 'w') as json_formatted:
            jsonobj = json.dumps(targetsDict)
            json_formatted.write("var jsonstr = '{}'".format(jsonobj))
            json_formatted.close()
