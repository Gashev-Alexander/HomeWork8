# модуль поиска контакта

from export_data_stud import export_data_stud
from print_data_stud import print_data_stud
from export_data_chit import export_data_chit
from print_data_chit import print_data_chit

def search_data(word, data, data1):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item    
    if len(data1) > 0:
        for item in data1:
            if word in item:
                return item
    else:
        return None