import csv

file = []
cleanFile = []

with open('Table14_2012_add.csv') as f:
	csvReader = csv.reader(f)
	for row in csvReader:
		file.append(row)

cleanFile = file

for i in range(1,len(file)):

	state = file[i][0].strip()
	agencyType = file[i][1].strip()
	agencyName = file[i][2].strip()
	q01 = file[i][3].strip()
	q02 = file[i][4].strip()
	q03 = file[i][5].strip()
	q04 = file[i][6].strip()
	population = file[i][7].strip()
	whereFrom = file[i][8].strip()

	if state == "":
		cleanFile[i][0] = file[i-1][0].strip()




	# if (file[i][j].strip() == ""):
	# 	cleanFile[i][j] = file[i-1][j].strip


with open("t13_add_2012.csv","w+") as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanFile)
