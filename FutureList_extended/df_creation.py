import pandas as pd
import time
from jikanscrap import get_data
import numpy as np
import json

datas = {}

with open('config.json') as json_data:
    datas = json.load(json_data)


data_cols = datas['data_cols'] + datas['aggregated'] + datas['type'] + datas['source'] + datas['percentages'] + datas['genres']

def create_df():
    df = pd.DataFrame()

    for c in data_cols:
        df[c] = 0

    df['name'] = ''

    df.to_csv('data/data.csv')

create_df()
