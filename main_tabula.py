from conf import conf_environment
import table_format as tf
import tabula

def main():
    confs = conf_environment()
    file_path = confs['file_path']
    destiny_path = confs['destiny_path']

    tables = tabula.read_pdf(file_path, pages='all', encoding='utf-8', pandas_options={'header': None})
    table_count = 1

    for table in tables:
        file_name = (
            'tabula'
            + str(table_count)
        )

        #Gets the desired text format and exports the data
        tf.clean_data(table)
        table.to_csv(destiny_path + file_name + '.csv')
        print(file_name + ' exported!')
        table_count+=1
    
    return