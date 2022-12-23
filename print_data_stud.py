def print_data_stud(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Номер группы".center(25), "Отделение".center(45), "Доп.Информация".center(30))
        print("-"*150)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(25), item[3].center(45), item[4].center(30))
    else:
        print("Справочник пуст!")