import csv
from datetime import datetime, time, timedelta

month = [	{'start' : '04/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '04/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '05/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '05/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '06/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '06/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '10/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '10/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '11/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '11/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '12/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '12/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '13/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '13/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '14/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '14/05/22 13:00', 'delta' : '03:00:00'},
			{'start' : '16/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '16/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '17/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '17/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '18/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '18/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '19/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '19/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '20/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '20/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '23/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '23/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '24/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '24/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '25/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '25/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '26/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '26/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '27/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '27/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '30/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '30/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '31/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '31/05/22 13:00', 'delta' : '04:00:00'},
		]

month330 = [	{'start' : '04/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '04/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '05/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '05/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '06/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '06/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '10/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '10/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '11/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '10/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '12/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '12/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '13/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '13/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '14/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '14/05/22 12:20', 'delta' : '03:00:00'},
			{'start' : '16/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '16/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '17/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '17/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '18/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '18/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '19/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '19/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '20/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '20/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '23/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '23/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '24/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '24/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '25/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '25/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '26/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '26/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '27/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '27/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '30/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '30/05/22 12:20', 'delta' : '04:00:00'},
			{'start' : '31/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '31/05/22 12:20', 'delta' : '04:00:00'},
		]

day = [	{'start' : '22/04/22 08:00', 'delta' : '04:00:00'}, {'start' : '22/04/22 13:00', 'delta' : '04:00:00'}]

workers = ['Атрошкин Евгений Леонидович',
'Беспалов Андрей Владимирович',
'Булай Олег Валентинович',
'Быков Михаил Константинович',
'Войтик Сергей Александрович',
'Германов Глеб Сергеевич',
'Голощев Александр Иванович',
'Горячко Максим Ростиславович',
'Горячко Сергей Ростиславович',
'Жаворонков Николай Николаевич',
'Ионов Александр Анатольевич',
'Коваленко Евгений Анатольевич',
'Кучко Дмитрий Антонович',
'Лабацевич Владислав Сергеевич',
'Литвинович Егор Анатольевич',
'Масалов Юрий Николаевич',
'Мастыко Владислав Валентинович',
'Метла Сергей Леонидович',
'Пашкевич Александр Александрович',
'Петрачков Игорь Эдуардович',
'Поляков Андрей Викторович',
'Ремберг Александр Сергеевич',
'Саулич Алексей Петрович',
'Саулич Сергей Петрович',
'Семененков Александр Сергеевич',
'Семененков Игорь Александрович',
'Сенькин Андрей Владимирович',
'Солдатенков Владислав Дмитриевич',
'Тымуль Максим Игнатьевич',
'Фёдоров Андрей Геннадьевич',
'Хмелевский Вячеслав Игоревич',
'Хуртов Денис Иванович',
'Чернов Илья Олегович',
'Шерегов Павел Петрович',
'Януш Виктор Михайлович']

class Time_range:
    def __init__(self, start, delta):
        self.__start = start
        self.__delta = delta

    def __eq__(self, other):
        return self.__start == other.__start and (
                self.__delta == other.__delta)

    @property
    def delta(self):
        return self.__delta

    @delta.setter
    def delta(self, delta):
        self.__delta = delta

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__start + self.__delta

    @property
    def date(self):
        return self.__start.date()

    def __str__(self):
        return str(self.__start.date()) + '\t' + str(self.__delta)

    def encode(self):
        return dict(start=str(self.__start), delta=str(self.__delta))

    @staticmethod
    def decode(dict_time_range):
        hours,minutes,seconds = map(int, dict_time_range['delta'].split(':'))
        return Time_range(datetime.strptime(dict_time_range['start'], '%d/%m/%y %H:%M'),
                                    timedelta(hours=hours, minutes=minutes, seconds=seconds))

def cross(time1, time2):
	"""Возвращает пересечение объектов Time_range"""
	ls = []
	if time1.start > time2.start:
		if time1.end == time2.end:
			ls.append(Time_range(time1.start, time1.delta))
		elif time1.start < time2.end < time1.end:
			ls.append(Time_range(time1.start, time2.end - time1.start))
		elif time1.start >= time2.end:
			pass
		else:
			ls.append(Time_range(time1.start, time1.delta))
	if time1.start == time2.start:
		if time2.end == time1.end:
			ls.append(time2)
		elif time2.end > time1.end:
			ls.append(Time_range(time2.start, time1.delta))
		else:
			ls.append(time2)
			ls.append(Time_range(time2.end, time1.end - time2.end))
	if time1.start < time2.start:
		if time2.end == time1.end:
			ls.append(Time_range(time1.start, time1.delta - time2.delta))
			ls.append(time2)
		elif time2.end < time1.end:
			ls.append(time2)
	if (time2.end > time1.end) and (time1.start < time2.start < time1.end):
		ls.append(Time_range(time1.start, time2.start - time1.start))
		ls.append(
			Time_range(time2.start, time1.end - time2.start))
	if time1.end <= time2.start:
		pass
	return ls

class WorkMonth:
	def __init__(self, month):
		self.__list_times = []
		for item in month:
			self.__list_times.append(Time_range.decode(item))

	@property
	def lt(self):
		return self.__list_times

class ActualWorkTimeWorker:
	def __init__(self, num_month, worker):
		with open('Проходная.csv', "r", newline="", encoding='utf-8') as file:
			reader = csv.reader(file)
			self.__events = []
			for row in reader:
				if worker in row[1]:
					inside = 'Вход' in row[1] or 'Въезд' in row[1]
					outside = 'Выход' in row[1] or 'Выезд' in row[1]
					if inside or outside:
						moment = datetime.strptime(row[0], '%H:%M:%S %d.%m.%y')
						if moment.month == num_month:
							self.__events.append([moment, True if inside else False])
		for d in self.__events:
			if self.__events.count(d) >1:
				self.__events.remove(d)
		self.__times_inside_work = []
		inside = False
		start = False
		for event in self.__events:
			if event[1]:
				start = event[0]
				inside = True
			else:
				if inside:
					delta = event[0] - start
					inside = False
			if not inside and start:
				self.__times_inside_work.append(Time_range(start, delta))
				start = False

	@property
	def lt(self):
		return self.__times_inside_work

work_time = WorkMonth(month)
for man in workers:
	human = ActualWorkTimeWorker(5, man)
	print(man)
	time_line = []
	for t in work_time.lt:
		for h in human.lt:
			c = cross(t, h)
			if len(c):
				for i in c:
					time_line.append(i)
	group = {}
	for i in time_line:
		if i.date in group:
			group[i.date] += i.delta
		else:
			group[i.date] = i.delta
	for key, value in group.items():
		print(key, value)
