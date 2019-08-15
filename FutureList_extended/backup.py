import pandas as pd
import json

def create_backup():
    df = pd.read_csv('data/data.csv').drop('Unnamed: 0', axis=1)

    df.to_csv('data/data_back.csv')

    datas = {}

    with open('data/params.json') as json_data:
        datas = json.load(json_data)

    with open("data/params_back.json", "w") as jsonFile:
        json.dump(datas, jsonFile)
