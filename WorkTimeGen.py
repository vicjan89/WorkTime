import csv
from datetime import datetime, time, timedelta

month = [	{'start' : '04/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '04/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '05/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '05/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '06/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '06/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '10/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '10/05/22 13:00', 'delta' : '04:00:00'},
			{'start' : '11/05/22 08:00', 'delta' : '04:00:00'}, {'start' : '10/05/22 13:00', 'delta' : '04:00:00'},
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

    def __str__(self):
        return str(self.__start) + ' ' + str(self.__start + self.__delta)

    def encode(self):
        return dict(start=str(self.__start), delta=str(self.__delta))

    @staticmethod
    def decode(dict_time_range):
        hours,minutes,seconds = map(int, dict_time_range['delta'].split(':'))
        return Time_range(datetime.strptime(dict_time_range['start'], '%d/%m/%y %H:%M'),
                                    timedelta(hours=hours, minutes=minutes, seconds=seconds))

def cross(cls, time_free, time_task):
	"""Возвращает список объектов Time_range заполняющих time_free и остаток от неразмещённой задачи time_task.
	Если time_free и time_task не пересекаются то возвращает пустой список. Если time_task размещена полностью или
	находится ранее time_free то возвращает None."""
	ls = []
	if time_free.summary == '':
		if time_free.start > time_task.start:
			if time_free.end == time_task.end:
				ls.append(Time_range(time_free.start, time_free.delta, time_task.summary, time_task.description))
				remainder = None
			elif time_free.start < time_task.end < time_free.end:
				ls.append(Time_range(time_free.start, time_task.end - time_free.start, time_task.summary,
									 time_task.description))
				ls.append(Time_range(time_task.end, time_free.end - time_task.end))
				remainder = None
			elif time_free.start >= time_task.end:
				remainder = None
			else:
				ls.append(Time_range(time_free.start, time_free.delta, time_task.summary, time_task.description))
				remainder = Time_range(time_free.end, time_task.end - time_free.end, time_task.summary,
									   time_task.description)
		if time_free.start == time_task.start:
			if time_task.end == time_free.end:
				ls.append(time_task)
				remainder = None
			elif time_task.end > time_free.end:
				remainder = Time_range(time_free.end, time_task.end - time_free.end, time_task.summary,
									   time_task.description)
				ls.append(Time_range(time_task.start, time_free.delta, time_task.summary, time_task.description))
			else:
				remainder = None
				ls.append(time_task)
				ls.append(Time_range(time_task.end, time_free.end - time_task.end))
		if time_free.start < time_task.start:
			if time_task.end == time_free.end:
				ls.append(Time_range(time_free.start, time_free.delta - time_task.delta))
				ls.append(time_task)
				remainder = None
			elif time_task.end < time_free.end:
				ls.append(Time_range(time_free.start, time_task.start - time_free.start))
				ls.append(time_task)
				ls.append(Time_range(time_task.end, time_free.end - time_task.end))
				remainder = None
		if (time_task.end > time_free.end) and (time_free.start < time_task.start < time_free.end):
			ls.append(Time_range(time_free.start, time_task.start - time_free.start))
			ls.append(
				Time_range(time_task.start, time_free.end - time_task.start, time_task.summary, time_task.description))
			remainder = Time_range(time_free.end, time_task.end - time_free.end, time_task.summary,
								   time_task.description)
		if time_free.end <= time_task.start:
			remainder = time_task
	else:
		remainder = time_task
	return ls, remainder

'''
class WorkDay:
	def __init__(self, before_lunch: Time_range, after_lunch: Time_range):
		self.__before_lunch = before_lunch
		self.__after_lunch = after_lunch

    def encode(self):
        return dict(self.__before_lanch.encode(), self.__after_lanch.encode())

    @staticmethod
    def decode(dict_time_range):
        hours,minutes,seconds = map(int, dict_time_range['delta'].split(':'))
        return Time_range(datetime.strptime(dict_time_range['start'], '%d/%m/%y %H-%M'
                                    ),timedelta(hours=hours, minutes=minutes, seconds=seconds))
'''

class WorkMonth:
	def __init__(self, month):
		self.__list_times = []
		for item in month:
			self.__list_times.append(Time_range.decode(item))

piple = WorkMonth(month)
i = input()
