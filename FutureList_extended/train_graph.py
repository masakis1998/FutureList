import pandas as pd
import re


def train_graph():

    df = pd.read_csv('data/train.csv')

    for title in df['name'].values:
        if (re.search(',', title)):
            df.loc[df['name'] == title, 'name'] = title.replace(',', '')

    df.to_csv('data/train_graph.csv')
