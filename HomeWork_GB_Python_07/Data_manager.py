import Data_provider
from datetime import datetime
from View_Module import PrintStringSheet

def ReadTimeSheet():
    return Data_provider.ReadTimeSheetFile()

def DeleteTimeSheet(all_sheet = False):
    if all_sheet:
        Data_provider.DeleteAllDataFromSheet()
    else:
        Data_provider.DeleteDataFromSheet()

def AddToDataSheet(change = False):
    if change:
        Data = ReadTimeSheet()
        while True:
            try:
                value = int(input("Введите номер записи для изменения: "))
                print("Данну запись вы хотите изменить?:", end=" ")
                PrintStringSheet(value, Data)
                while True:
                    resultValue = int(input("Введите 0 для отмены или 1 для изменения: "))
                    if resultValue == 0 or resultValue == 1:
                        if resultValue == 0:
                            return
                        else: 
                            Data[value][1] = input("Введите изменения: ")
                            Data_provider.WriteNewDataInSheet(Data)
                            return
                    else:
                        print("Попробуйте еще раз")
            except :
                print("Что то пошло не так, попробуйте снова")
                value = int(input("Если хотите отменить операцию, нажмите 0: "))
                if value == 0:
                    return
                else:
                    continue
    else:
        Data = ReadTimeSheet()
        new_data = []
        while True:
            try:
                new_datetime = datetime.strptime(input("Введите дату события в формате 30.12.2000: "), "%d.%m.%Y").date().strftime("%d.%m.%Y")
                print(f"Вы ввели {new_datetime}")
                new_string = input("Введите событие: \n")
                result = False
                for i in range(len(Data)):
                    if Data[i][0] <= new_datetime:
                        new_data.append(Data[i])
                    elif not result and Data[i][0] >= new_datetime:
                        new_data.append((new_datetime,new_string))
                        new_data.append(Data[i])
                        result = True
                    else:
                        new_data.append(Data[i])
                Data_provider.WriteNewDataInSheet(new_data)
                return
            except :
                print("Что то пошло не так, попробуйте снова")
                value = int(input("Если хотите отменить операцию, нажмите 0: "))
                if value == 0:
                    return
                else:
                    continue

def ChangeSheet():
    AddToDataSheet(True)
