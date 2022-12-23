
from import_data_stud import import_data_stud
from import_data_chit import import_data_chit
from export_data_stud import export_data_stud
from export_data_chit import export_data_chit
from print_data_chit import print_data_chit
from print_data_stud import print_data_stud
from search_data import search_data




def greeting():
    print("База данных Забайкальского Горного колледжа")

def input_data_stud():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    group_user = input("Введите Номер Группы: ")
    otdel = input("Введите Отделение: ")
    note = input("Введите Дополнительную информацию: ")
    return [last_name, first_name, group_user, otdel, note]

def input_data_chit():
    chit_last_name = input("Введите фамилию: ")
    chit_first_name = input("Введите имя: ")
    dis_chit = input("Введите дисциплину: ")
    note_chit = input("Введите дополнительную информацию: ")
    return [chit_last_name, chit_first_name, dis_chit, note_chit]

def update_data():
    print('тут будет редактирование')

def choice_sep():
    sep = "/"

def choice_todo():
    print("Какой раздел вас интересует?:\n\
    1 - Добавить Студента \n\
    2 - Добавить Преподавателя \n\
    3 - Вывод списков \n\
    4 - Поиск по фамилии")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = choice_sep()
        import_data_stud(input_data_stud(), sep)
    elif ch == '2':
        sep = choice_sep()
        import_data_chit(input_data_chit(), sep)
    elif ch == '3':
        print("Выберите интересующую таблицу: \n\
        1 - Студенты \n\
        2 - Преподаватели ")
        ch_s = input("Введите цифру: ")
        if ch_s == '1':
            data = export_data_stud()
            print_data_stud(data)
        elif ch_s == '2':
            data = export_data_chit()
            print_data_chit(data)
        else:
            print("Это так не работает!")
    elif ch == '4':
        word = input("Введите данные для поиска: ")
        data = export_data_chit() 
        data1 = export_data_stud()
        item = search_data(word, data, data1)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Группа или Дисциплина".center(35))
            print("-"*75)
            print(item[0].center(20), item[1].center(20), item[2].center(35))
            ch_d = input('Введите 1 если хотите изменить запись: ')
            if ch_d == '1':
                ch_d = update_data()
            else:
                print('Повторите попытку!')        
        else:
            print("Данные не обнаружены")