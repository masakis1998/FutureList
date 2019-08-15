import pandas as pd
import re


def test_graph():

    df = pd.read_csv('data/test.csv')

    prediction = pd.read_csv('data/final_data.csv')

    for title in df['name'].values:
        if (re.search(',', title)):
            df.loc[df['name'] == title, 'name'] = title.replace(',', '')

    for mal_id in df['id_ref'].values:
        df.loc[df['id_ref'] == mal_id, 'score'] = prediction.loc[prediction['id_ref'] == mal_id, 'prediction'].values[0]

    df.to_csv('data/test_graph.csv')
