from conf import conf_environment
import table_format as tf
import camelot

def export_tables(tables: camelot.core.TableList, destiny_path:str, table_type: str):
    for table in tables:
        report = table.parsing_report
        file_name = (
            'camelot_'
            + table_type 
            + str(report['order']) 
            + '_' 
            + str(report['page'])) 
        
        #Exporting rules: only high accuracy tables
        if report['accuracy'] > 90:
            #Gets the desired text format and exports the data
            tf.clean_data(table.df)
            table.to_csv(destiny_path + file_name + '.csv')
            print(file_name + ' exported with ' + str(report['accuracy']) + r'% accuracy!')
        
    return

def main():
    confs = conf_environment()
    file_path = confs['file_path']
    destiny_path = confs['destiny_path']
    
    #If the table has line segments in the background
    tables_background = camelot.read_pdf(file_path, pages='1-end', process_background=True)

    if len(tables_background) > 0:
        export_tables(tables_background, destiny_path, "bg")

    #If the table has line segments in the foreground
    tables_foreground = camelot.read_pdf(file_path, pages='1-end')
    
    if len(tables_foreground) > 0:
        export_tables(tables_foreground, destiny_path, "fg")

    return