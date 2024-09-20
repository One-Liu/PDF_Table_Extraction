'''This file is for calling all the other files'''
import main_camelot as cam
import main_pdfplumber as plum
import main_tabula as tab

def main():
    '''Calls all the other files'''
    cam.main()
    plum.main()
    tab.main()
    return

if __name__ == '__main__':
    main()
