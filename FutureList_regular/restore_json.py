import json

def restore():
    datas = {}

    with open('data/params_back.json') as json_data:
        datas = json.load(json_data)

    with open("data/params.json", "w") as jsonFile:
        json.dump(datas, jsonFile)

restore()
