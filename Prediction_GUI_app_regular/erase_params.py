import json
import sys

num = int(sys.argv[1])

data = []

with open('data/params.json', 'r') as json_data:
    data = json.load(json_data)

data = data['params']
data.remove(data[num])
datas = {'params': data}

with open('data/params.json', 'w') as json_data:
    json.dump(datas, json_data)
