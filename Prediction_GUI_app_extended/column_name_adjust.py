import pandas as pd
import re

def process_column_name():

    df = pd.read_csv('data/data.csv').drop('Unnamed: 0', axis=1)

    regex = re.compile(r"\[|\]|<|,", re.IGNORECASE)

    df.columns = [regex.sub("_", col) if any(x in str(col) for x in set(('[', ']', '<', ','))) else col for col in df.columns.values]

    df.to_csv('data/data_processed.csv')
