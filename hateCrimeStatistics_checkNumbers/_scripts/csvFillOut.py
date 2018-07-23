#!/usr/bin/env python3
import csv
year = 2016
table = '14'
with open('../02_csv_column_clean/hcs_'+str(year)+'_table'+table+'.csv', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]
rows[0] = ["state", "agencyType", "agencyName", "quarter01", "quarter02", "quarter03", "quarter04", "population"]
rows_clean = rows

for i in range(0,len(rows)):
	row = rows[i]
	prev = rows[i-1]
	cleanrow = rows_clean[i]

	state = row[0]
	agencyType = row[1]
	agencyName = row[2]

	if not state:
		cleanrow[0] = prev[0]
	if not agencyType:
		cleanrow[1] = prev[1]
	if not agencyName:
		cleanrow[2] = "@@DELETE ME@@"


with open('../03_csv_filled_out/hcs_'+str(year)+'_table'+table+'.csv','w+') as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(rows_clean)