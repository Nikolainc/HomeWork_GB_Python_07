from datetime import datetime

def printTimeSheet(time_sheet, all_sheets = False, only_past_sheet = False):
    today = datetime.today().strftime("%d.%m.%Y")
    print(f"\nСегодня: {today}\n")
    if time_sheet[0] == "":
        print("Записей нет\n")
        return
    if all_sheets:
        for i in range(len(time_sheet)):
            PrintStringSheet(i,time_sheet)
    elif only_past_sheet:
        for i in range(len(time_sheet)):
            if today > time_sheet[i][0]:
                PrintStringSheet(i,time_sheet)
    else:
        for i in range(len(time_sheet)):
            if today <= time_sheet[i][0]:
                PrintStringSheet(i,time_sheet)
    print("\n")



def PrintStringSheet(ids, time_sheet):
    print(f"Запись N{ids} : ", end=" ")
    print(" ".join(time_sheet[ids]))