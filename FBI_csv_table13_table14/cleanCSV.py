import csv

file = []
cleanFile = []
with open('1_annualCSV/hateCrimeStatistics_2010.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		file.append(row)

cleanFile = file

for i in range(0,len(file)):
	year = file[i][0].strip()
	state = file[i][1].strip()
	agencyType = file[i][2].strip()
	agencyName = file[i][3].strip()
	# q1 = file[i][4].strip()
	# q2 = file[i][5].strip()
	# q3 = file[i][6].strip()
	# q4 = file[i][7].strip()
	# population = file[i][8].strip()


	if (year == "") or (year == "2010"):
		cleanFile[i][0] = "2010"

	if state == "Nan":
		cleanFile[i][1] = file[i-1][1]
	
	if agencyType == "Nan":
		cleanFile[i][2] = file[i-1][2]
	
	if agencyName == "Nan":
		cleanFile[i][3] = "@@DELETE ME@@"


with open("fbi2010.csv","w+") as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanFile)
