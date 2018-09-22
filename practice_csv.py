employee = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

import csv
with open('list.csv', 'w', encoding='utf-8') as man:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(man, fields, delimiter=';')
	writer.writeheader()
	for man in employee:
		writer.writerow(man)