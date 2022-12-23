def print_data_chit(data):
    if len(data) > 0:
        print("Фамилия".center(25), "Имя".center(20), "Дисциплина".center(25), "Доп.Информация".center(50))
        print("-"*130)
        for item in data:
            print(item[0].center(25), item[1].center(20), item[2].center(25), item[3].center(45))
    else:
        print("Справочник пуст!")