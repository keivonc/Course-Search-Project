import json

data = open('/JSON/JSON.json').read() #opens the json file and saves the raw contents
jsonData = json.loads(data) #converts to a json structure
