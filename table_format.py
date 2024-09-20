'''This file is for the functions that clean the data'''
from pandas import DataFrame

def replace_values(text):
    '''Replaces values in columns'''
    if isinstance(text) == str:
        text = text.replace('\n',' ').replace('\r',' ')
    return text

def clean_data(df: DataFrame):
    '''Main function for cleaning data'''
    for column in df:
        df[column] = df[column].apply(replace_values)

def drop_empty_columns(df: DataFrame):
    '''Replaces empty strings with None and then drops empty columns'''
    df = df.replace({'': None})
    df.dropna(axis=1, how='all', inplace=True)
