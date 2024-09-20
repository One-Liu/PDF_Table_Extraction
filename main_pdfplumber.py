'''This file is for the table extraction with pdfplumber'''
import pdfplumber
import pandas as pd
from conf import conf_environment
import table_format as tf

def main():
    '''Extracts and exports the table'''
    confs = conf_environment()
    file_path = confs['file_path']
    destiny_path = confs['destiny_path']

    table_count = 1
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            for table in page.extract_tables(table_settings={}):
                table = pd.DataFrame(table)
                file_name = (
                    'pdfplumber'
                    + str(table_count))

                tf.drop_empty_columns(table)

                #Exporting rules: ignores empty tables
                if len(table.columns) > 0:
                    #Gets the desired text format and exports the data
                    tf.clean_data(table)
                    table.to_csv(destiny_path + file_name + '.csv')
                    print(file_name + ' exported!')
                    table_count+=1
