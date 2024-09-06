import re
import os

def conf_environment() -> dict:
    with open('paths.txt', 'rt', encoding='utf-8') as conf:
        pdf_test_conf = conf.read()

    confs = {}
    match_file_path = re.search(r'path = ([\S]+)', pdf_test_conf)
    match_destiny_path = re.search(r'destiny = ([\S]+)', pdf_test_conf)
    
    if not match_file_path:
        print('Origin path was not specified')
        exit()
    if not match_destiny_path:
        print('Destiny path was not specified')
        exit()
    
    file_path = match_file_path.group(1)
    destiny_path = match_destiny_path.group(1)

    if not os.path.exists(destiny_path):
        os.makedirs(destiny_path)
        print('Directory created:',destiny_path)

    confs['file_path'] = file_path
    confs['destiny_path'] = destiny_path

    return confs