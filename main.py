import csv
from datetime import datetime, time, timedelta
import calendar

data = []
tabel = []
persons = []

F_TIMEWORK = 'Проходная.csv'
F_PERSONS = 'Персонал.csv'
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
    d[0] = datetime.strptime(d[0], '%H:%M:%S %d.%m.%y')
    h = d[0].hour
    m = d[0].minute
    if d[1].find('ПС 330') == -1:
        if (h >= 8 and h < 12) or (h >= 13 and h < 17):
            print(d)
    else:
        if (h >= 8 and h < 12) or (h >= 13 and h < 17 and m <= 20):
            print(d)

print('Табель')
s1 = time(8, 0, 0)
e1 = time(12, 0, 0)
s2 = time(13, 0, 0)
e2 = time(17, 0, 0)
month = calendar.Calendar()
for p in persons:
    for day in month.itermonthdates(2021, 10):
        LongTime = time()

        into = False
        out = False
        for wt in data:
            if wt[0].date() == day and p[0] in wt[1]:
                if 'Вход' in wt[1] or 'Въезд' in wt[1]:
                    into = True
                    st = wt[0]
                elif 'Выход' in wt[1] or 'Выезд' in wt[1]:
                    out = True
                    en = wt[0]
                else:
                    print(wt, 'Непонятное событие')
            if into and out:
                into = False
                out = False
                if st < s1 and en < e1 and en > s1:
                    LongTime = en - st
        w = day.weekday()
        if w != 5 and w != 6 and day.month == 10:
                print(day, p, LongTime)
