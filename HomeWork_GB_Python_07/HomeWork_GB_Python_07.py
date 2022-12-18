#Сделать программу расписание - делаем расписание занятий\тренировок или что-то своё.
#Для хранения информации используем текстовые файлы (сохраняем, перезаписываем в них и т.д.) , бесконечный цикл, функции и прочий функционал.
#Программа будет, как консольный бот, который будет нас спрашивать что и как нужно сделать - вывести, показать, перезаписать , добавить событие в определенный день недели

import Data_manager
import View_Module

def MenuSelecter():
    dectionary = {'+': 0, '-': 1, '=': 2, '*': 3, '~': 4, '0': 5, '1': 6}
    print("Вывести предстоящие мероприятия: '+'")
    print("Вывести прошедшие мероприятия: '-'")
    print("Вывести все записи: '='")
    print("Удалить запись: '*'")
    print("Добавить запись: '~'")
    print("Удалить все: '0'")
    print("Выход: '1'")

    while True:
        find = True
        inputmenu = str(input(">> "))
        for i in dectionary.keys():
            if i != inputmenu:
                find = False
                continue
            else:
                return dectionary.get(inputmenu)
        if not find:
            print("Такого нет в меню")

print("Журнал\n")

while True:
    select = MenuSelecter()
    if select == 0:
        View_Module.printTimeSheet(Data_manager.ReadTimeSheet())
    elif select == 1:
        View_Module.printTimeSheet(Data_manager.ReadTimeSheet(), only_past_sheet = True)
    elif select == 2: 
        View_Module.printTimeSheet(Data_manager.ReadTimeSheet(), all_sheets = True)
    elif select == 3:
        Data_manager.DeleteTimeSheet()
    elif select == 4:
        pass
    elif select == 5:
        Data_manager.DeleteTimeSheet(all_sheet = True)
    elif select == 6:
        break
