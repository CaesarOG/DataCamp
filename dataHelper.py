#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory
import os #code below reads in all DataCamp data used in a notebook
import sys
dirname = sys.argv[1]
def typesMap(dataType, val):
    if dataType == 'float':
        return float(val)
    if dataType == 'str':
        return val
    if dataType == 'int':
        return int(val)

for filename in os.listdir("./Datasets"+dirname):
    if filename.endswith(".json"): #list data
        fileDropExt = filename.split('.')[0]
        name, dataType = fileDropExt.split('-')[0], fileDropExt.split('-')[1]
        globals()[name] = []
        inp = open("./Datasets"+dirname+filename, "r")
        for line in inp.readlines():
            for i in line.split(","):
                globals()[name].append(typesMap(dataType, i))
        inp.close()

#https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-run
#https://stackoverflow.com/questions/25491541/python3-json-post-request-without-requests-library
#standard docs -> urllib.request.urlencode({"data": var_name}).encode('utf8') wont work since that returns application/x-www-form-urlencoded
'''
import urllib
import json

data = json.dumps({"_pop-float": pop}).encode('utf8')
headers = {"Content-Type": "application/json"}
req = urllib.request.Request("http://startupxchangeapi.tk/api/getData", data, headers)
res = urllib.request.urlopen(req).read()
res
'''