# Import `os`
import csv
import os

FILENAME = r'C:\Users\Виктор\PycharmProjects\purchases\Закупки.csv'
# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
cwd

with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

