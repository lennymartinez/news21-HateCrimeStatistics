#!/usr/bin/env python3
import csv

with open('../hcs_untidy.csv', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]

tidy = []
header = ["year","state","city","quarter","incidentsReported","population"]
tidy.append(header)
# print(header)

for row in rows[1:]:
	state = row[0]
	city = row[1]
	q1 = row[2]
	q2 = row[3]
	q3 = row[4]
	q4 = row[5]
	population = row[5]
	year = row[6]

	out1 = [year,state,city,1,q1,population]
	out2 = [year,state,city,2,q2,population]
	out3 = [year,state,city,3,q3,population]
	out4 = [year,state,city,4,q4,population]
	# print(out1)
	# print(out2)
	# print(out3)
	# print(out4)

	tidy.append(out1)
	tidy.append(out2)
	tidy.append(out3)
	tidy.append(out4)

with open('../hcs_tidy.csv','w+') as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(tidy)