import csv
from datetime import datetime, time, timedelta

data = []
tabel = []
persons = []
away = []
period = 0.0

F_TIMEWORK = 'Проходная.csv'
F_PERSONS = 'Персонал.csv'
F_AWAY = 'Отсутствия.csv'

with open(F_AWAY, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        away.append(row)
        away[-1][0] = datetime.strptime(away[-1][0], '%d.%m.%y').date()
        away[-1][1] = datetime.strptime(away[-1][1], '%d.%m.%y').date()

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

for d in data:
    if data.count(d) >1:
        data.remove(d)


print('Табель')
s1 = timedelta(hours=8, minutes=0, seconds=0)
e1 = timedelta(hours=12, minutes=0, seconds=0)
s2 = timedelta(hours=13, minutes=0, seconds=0)
e2 = timedelta(hours=17, minutes=0, seconds=0)
s3 = timedelta(hours=12, minutes=20, seconds=0)
e3 = timedelta(hours=16, minutes=20, seconds=0)

month = calendar.Calendar()

for p in persons:
    for day in month.itermonthdates(2022, 3):
        LongTime = timedelta()
        period = 0.0
        into = False
        out = False
        tabel.append([day, p,  ''])
        for wt in data:
            if wt[0].date() == day and p[0] in wt[1]:
                if 'Вход' in wt[1] or 'Въезд' in wt[1]:
                    into = True
                    st = wt[0]
                elif 'Выход' in wt[1] or 'Выезд' in wt[1]:
                    if into:
                        out = True
                        en = wt[0]
                else:
                    print(wt, 'Непонятное событие')
            if into and out:
                into = False
                out = False
                LongTime = timedelta()
                st_time = timedelta(hours=st.hour, minutes=st.minute, seconds=st.second)
                en_time = timedelta(hours=en.hour, minutes=en.minute, seconds=en.second)
                if st_time < s1 and en_time < e1 and en_time > s1:
                    LongTime = LongTime + en_time - s1
                if st_time < s1 and en_time > e1:
                    LongTime = LongTime + e1 - s1
                if st_time > s1 and en_time > e1 and st_time < e1:
                    LongTime = LongTime + e1 - st_time
                if st_time > s1 and en_time < e1:
                    LongTime = LongTime + en_time - st_time
                if 'ПС 330' in wt[1]:
                    if st_time < s3 and en_time < e3 and en_time > s3:
                        LongTime = LongTime + en_time - s3
                    if st_time < s3 and en_time > e3:
                        LongTime = LongTime + e3 - s3
                    if st_time > s3 and en_time > e3 and st_time < e3:
                        LongTime = LongTime + e3 - st_time
                    if st_time > s3 and en_time < e3:
                        LongTime = LongTime + en_time - st_time
                else:
                    if st_time < s2 and en_time < e2 and en_time > s2:
                        LongTime = LongTime + en_time - s2
                    if st_time < s2 and en_time > e2:
                        LongTime = LongTime + e2 - s2
                    if st_time > s2 and en_time > e2 and st_time < e2:
                        LongTime = LongTime + e2 - st_time
                    if st_time > s2 and en_time < e2:
                        LongTime = LongTime + en_time - st_time
                period = period + LongTime.seconds/60/60
        tabel[-1][2] = str(period)
for t in tabel:
    for d in away:
  #      print(type(d[0]), type(t[0]))
        if d[2] == str(t[1][0]) and d[0] <= t[0] and d[1] >= t[0]:
#            print(d[3])
            t[2] = d[3]
for t in tabel:
    if t[0].month == 3 and t[0].day <= 31 and t[0].weekday() != 5 and t[0].weekday() != 6 and t[2] != '8.0':
        print(t[0], t[1], t[2])
