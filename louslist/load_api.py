import json
from urllib.request import urlopen

link = "https://luthers-list.herokuapp.com/api/dept/APMA/"

e = urlopen(link)
myfile = e.read()



f = open('JSON/department.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
#list
for i in data:
    for value in i.items():
        
        with open(value[1]+".json",'w') as f:
            f.write(myfile+value[1]+"/?format=json")
       

