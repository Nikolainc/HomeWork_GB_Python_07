from datetime import datetime
from View_Module import PrintStringSheet


_time_sheet_path = "/Users/Nikolai/source/repos/GB/HomeWork_GB_Python_07/HomeWork_GB_Python_07/TimeSheetData.txt"
_cleared = False

def ReadTimeSheetFile():
    global _time_sheet_path
    f = open(_time_sheet_path, 'r')
    data_list = f.read().split('\n')
    if data_list[0] == "":
        return data_list
    data_list = Splitter(data_list)
    f.close()
    return data_list

def Splitter(data):
    new_data = []
    for i in range(len(data)):
        new_data.append(data[i].split('='))
        new_data[i][0] = datetime.strptime(new_data[i][0], "%d.%m.%Y").date().strftime("%d.%m.%Y")
    new_data = dict(enumerate(new_data))
    return new_data

def WriteNewDataInSheet(Data):
    global _time_sheet_path
    f = open(_time_sheet_path, 'w')
    for i in range(len(Data)):
        if i < len(Data) - 1:
            f.write(f"{str(Data[i][0])}={str(Data[i][1])}\n")
        else:
            f.write(f"{str(Data[i][0])}={str(Data[i][1])}")
    f.close()

def DeleteAllDataFromSheet():
    global _time_sheet_path
    f = open(_time_sheet_path, 'w')
    f.close()

def DeleteDataFromSheet():
    Data = ReadTimeSheetFile()
    while True:
        value = int(input("Введите номер записи для удаления: "))
        if value < len(Data):
            print("Данну запись вы хотите удалить?:", end=" ")
            PrintStringSheet(value, Data)
            while True:
                resultValue = int(input("Введите 0 для отмены или 1 для удаления: "))
                if resultValue == 0 or resultValue == 1:
                    if resultValue == 0:
                        return
                    else: 
                        new_data = []
                        for i in range(len(Data)):
                            if i == value:
                                continue
                            new_data.append(Data[i])
                        WriteNewDataInSheet(new_data)
                        return
                else:
                    print("Попробуйте еще раз")
        else:
            print("Неверный номер записи")
            continue