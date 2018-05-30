import csv

with open('annualReports/hateCrimeStatistics_2016.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]

cleanRows = rows

for i in range(1,len(rows)):

	#clean year column, if a cell is empty, fill it with the year from the file name.file
	year = rows[i][0].strip()
	if (year == 'Nan') or (year == ''):
		cleanRows[i][0] = '2016'

	#clean the state name. if the state is 'Nan', 'NaN', or '' (empty) replace it with the value from above
	state = rows[i][1].strip()

	if (state == 'Nan') or (state == 'NaN') or (state == ''):
		cleanRows[i][1] = rows[i-1][1]
	
	#clean the agency type. if the type is Nan or empty (or variation), replace with value from above cell
	agencyType = rows[i][2].strip()

	if (agencyType == 'Nan') or (agencyType == 'NaN') or (agencyType == ''):
		cleanRows[i][2] = rows[i-1][2]

	#clean the agency name. if empty, or Nan, mark for deletion. it's probably part of a summary line from table13
	agencyName = rows[i][3].strip()

	if (agencyName == 'Nan') or (agencyName == 'NaN') or (agencyName == ''):
		cleanRows[i][3] = '@@Delete Me@@'

	#if agency has a colon at the end of the name, add a value to the last column so I can look at it manually.
	#if agency has a number at the end of the name, delete it from the name.
	endchar = agencyName[-1]
	if (endchar == '2') or (endchar == '3'):
		cleanRows[i][3] = agencyName[:-1]

	if (endchar == ':'):
		cleanRows[i][9] = '1'
	else:
		cleanRows[i][9] = '0'

	#clean the quarters. If you get an empty or a 'Nan' variation, replace with 'DNR'
	for j in range(4,8):
		quarter = rows[i][j].strip()
		if (quarter == '') or (quarter == 'Nan') or (quarter == 'NaN'):
			cleanRows[i][j] = 'DNR'

	#clean the population. If empty or Nan variation, replace with 'No Data'
	population = rows[i][8].strip()
	if (population == ''):
		cleanRows[i][8] = 'No Data'

#write the rows to an ouput file
with open('forCombining/hateCrimeStatistics2016.csv','w+') as f:
			csvWriter = csv.writer(f,delimiter=',')
			csvWriter.writerows(cleanRows)
