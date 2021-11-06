import csv
import datetime

data = []
# StartWork = datetime.datetime()
FILENAME = r'C:\Users\Виктор\PycharmProjects\WorkTime\Проходная.csv'
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

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


