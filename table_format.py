from pandas import DataFrame

def replace_values(text):
    if type(text) == str:
        text = text.replace('\n',' ').replace('\r',' ')
    return text

def clean_data(df: DataFrame):
    for column in df:
        df[column] = df[column].apply(replace_values)
    return

def drop_empty_columns(df: DataFrame):
    #Replaces empty strings with None so we can drop empty columns
    df = df.replace({'': None})
    df.dropna(axis=1, how='all', inplace=True)
    return