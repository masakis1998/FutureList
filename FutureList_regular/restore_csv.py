import pandas as pd

def restore():
    df = pd.read_csv('data/data_back.csv').drop('Unnamed: 0', axis=1)

    df.to_csv('data/data.csv')

restore()
