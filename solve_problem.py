import csv


def open_secret_file(path):
	"""Открыть файл"""
	with open(path, newline='\n') as csvfile:
	 spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	 return spamreader
	return 'Пусто'

if __name__ == '__main__':
	text = open_secret_file('metallo.txt')
	print (text)