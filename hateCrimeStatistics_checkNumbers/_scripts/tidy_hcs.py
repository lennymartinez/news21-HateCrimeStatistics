#!/usr/bin/env python3
import csv

with open('../hcs_untidy.csv', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]

tidy = []
header = ["year","state","city","population","quarter","incidentsReported"]
tidy.append(header)
# print(header)

for row in rows[1:]:
	state = row[1]
	city = row[2]
	q1 = row[4]
	q2 = row[5]
	q3 = row[6]
	q4 = row[7]
	population = row[3]
	year = row[0]

	out1 = [year,state,city,population,1,q1]
	out2 = [year,state,city,population,2,q2]
	out3 = [year,state,city,population,3,q3]
	out4 = [year,state,city,population,4,q4]
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