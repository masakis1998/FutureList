import pandas as pd
import time
from jikanscrap import get_data
from jikanscrap import get_stats
import numpy as np
import json

datas = {}

with open('config.json') as json_data:
    datas = json.load(json_data)

studio = datas['studio']
studio.append("Brain's Base")


def update_data():
    df = pd.read_csv('data/data.csv').drop('Unnamed: 0', axis=1)

    for mal_id in list(df[df['notDone'] == True]['id_ref'].values):
        timeout = time.time() + 2

        temp = get_data(mal_id)
        stats = get_stats(mal_id)

        if len(temp)>1:
            df.loc[df['id_ref'] == mal_id, 'name'] = temp['title']
            df.loc[df['id_ref'] == mal_id, 'mean'] = temp['score']
            df.loc[df['id_ref'] == mal_id, 'rank'] = temp['rank']
            df.loc[df['id_ref'] == mal_id, 'popularity'] = temp['popularity']
            df.loc[df['id_ref'] == mal_id, 'members'] = temp['members']
            df.loc[df['id_ref'] == mal_id, 'fav'] = temp['favorites']
            df.loc[df['id_ref'] == mal_id, 'ep'] = temp['episodes']

            try:
                df.loc[df['id_ref'] == mal_id, 'year'] = temp['aired']['from'][:4]
            except:
                df.loc[df['id_ref'] == mal_id, 'year'] = 0


            if temp['source'] == 'Manga' or temp['source'] == 'Webmanga' or temp['source'] == '4-komamanga':
                df.loc[df['id_ref'] == mal_id, 'Manga'] = 1

            if temp['source'] == 'Original':
                df.loc[df['id_ref'] == mal_id, 'Original'] = 1

            if temp['source'] == 'Book' or temp['source'] == 'Novel':
                df.loc[df['id_ref'] == mal_id, 'Novel'] = 1

            if temp['source'] == 'Light novel':
                df.loc[df['id_ref'] == mal_id, 'Lightnovel'] = 1

            if temp['source'] == 'Visual novel':
                df.loc[df['id_ref'] == mal_id, 'Visualnovel'] = 1

            if temp['source'] == 'Game' or temp['source'] == 'Cardgame':
                df.loc[df['id_ref'] == mal_id, 'Game'] = 1

            if temp['source'] == 'Picturebook' or temp['source'] == 'Unknown' or temp['source'] == 'Music':
                df.loc[df['id_ref'] == mal_id, 'Other_source'] = 1

            df.loc[df['id_ref'] == mal_id, 'fav/members'] = temp['favorites'] / temp['members']
            df.loc[df['id_ref'] == mal_id, 'rank/pop'] = temp['favorites'] / temp['popularity']

            df.loc[df['id_ref'] == mal_id, 'comp/members'] = stats['completed'] / temp['members']
            df.loc[df['id_ref'] == mal_id, 'dropped/members'] = stats['dropped'] / temp['members']

            try:
                df.loc[df['id_ref'] == mal_id, 'percent10'] = stats['scores']['10']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent9'] = stats['scores']['9']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent8'] = stats['scores']['8']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent7'] = stats['scores']['7']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent6'] = stats['scores']['6']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent5'] = stats['scores']['5']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent4'] = stats['scores']['4']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent3'] = stats['scores']['3']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent2'] = stats['scores']['2']['percentage']
            except:
                pass

            try:
                df.loc[df['id_ref'] == mal_id, 'percent1'] = stats['scores']['1']['percentage']
            except:
                pass

            if temp['type'] == 'Music':
                df.loc[df['id_ref'] == mal_id, 'Music_type'] = 1
            else:
                df.loc[df['id_ref'] == mal_id, temp['type']] = 1

            studio_array = []
            for s in temp['studio']:
                studio_array.append(s['name'])

            for s in studio_array:
                if s in set(studio):
                    df.loc[df['id_ref'] == mal_id, s] = 1
                else:
                    df.loc[df['id_ref'] == mal_id, 'Other'] = 1

            genre_array = []
            for g in temp['genre']:
                genre_array.append(g['name'])

            for g in genre_array:
                df.loc[df['id_ref'] == mal_id, g] = 1

            df.loc[df['id_ref'] == mal_id, 'notDone'] = False

        else:
            df = df[df['id_ref'] != mal_id]
        print(len(list(df[df['notDone'] == True]['id_ref'].values)))
        df.to_csv('data/data.csv')
        while(time.time() <= timeout):
            pass


    df.to_csv('data/data.csv')

    print('Finished updating data')
