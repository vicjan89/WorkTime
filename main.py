import csv
import datetime
import calendar

data = []

persons = []
# StartWork = datetime.datetime()
F_TIMEWORK = r'C:\Users\Виктор\PycharmProjects\WorkTime\Проходная.csv'
F_PERSONS = r'C:\Users\Виктор\PycharmProjects\WorkTime\Персонал.csv'
with open(F_TIMEWORK, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

with open(F_PERSONS, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        persons.append(row)

print('Передвижения во время работы')
for d in data:
    d[0] = datetime.datetime.strptime(d[0], '%H:%M:%S %d.%m.%y')
    h = d[0].hour
    m = d[0].minute
    if d[1].find('ПС 330') == -1 == -1:
        if (h >= 8 and h < 12) or (h >= 13 and h < 17):
            print(d)
    else:
        if (h >= 8 and h < 12) or (h >= 13 and h < 17 and m <= 20):
            print(d)

print('Нет отметки о приходе')
month = calendar.Calendar()
for p in persons:
    for day in month.itermonthdates(2021, 10):
        NotWork = True
        for wt in data:
            if wt[0].date() == day and p[0] in wt[1]:
                NotWork = False
        if NotWork:
            w = day.weekday()
            if w != 5 and w != 6 and day.month == 10:
                print(day, p)
