import Data_provider

def ReadTimeSheet():
    return Data_provider.ReadTimeSheetFile()

def DeleteTimeSheet(all_sheet = False):
    if all_sheet:
        Data_provider.DeleteAllDataFromSheet()
    else:
        Data_provider.DeleteDataFromSheet()
        
#11.11.2021=Что-то в прошлом
#20.12.2022=Поездка в Таиланд
#21.12.2022=Завтрак в Бангкоке
#21.12.2022=Поход в магазин
#21.12.2022=Массаж
#22.12.2022=Поездка на жд в Банг Сафан