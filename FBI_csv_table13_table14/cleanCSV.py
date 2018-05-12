import csv

file = []
cleanFile = []
with open('4_annualTestAlt/fbiMain_one.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		file.append(row)

cleanFile = file

for i in range(0,len(file)):
	pop10 = file[i][8].strip()
	pop11 = file[i][13].strip()
	pop12 = file[i][18].strip()
	pop13 = file[i][23].strip()
	pop14 = file[i][28].strip()
	pop15	= file[i][33].strip()
	pop16 = file[i][38].strip()
	
	if (pop10 == "") or (pop10 == "---") or (pop10 == "Nan"):
		cleanFile[i][8] = "Nan"
	
	if (pop11 == "") or (pop11 == "---") or (pop11 == "Nan"):
		cleanFile[i][13] = "Nan"

	if (pop12 == "") or (pop12 == "---") or (pop12 == "Nan"):
		cleanFile[i][18] = "Nan"

	if (pop13 == "") or (pop13 == "---") or (pop13 == "Nan"):
		cleanFile[i][23] = "Nan"

	if (pop14 == "") or (pop14 == "---") or (pop14 == "Nan"):
		cleanFile[i][28] = "Nan"

	if (pop15 == "") or (pop15 == "---") or (pop15 == "Nan"):
		cleanFile[i][33] = "Nan"

	if (pop16 == "") or (pop16 == "---") or (pop16 == "Nan"):
		cleanFile[i][38] = "Nan"	


with open("fbiMain_oneClean.csv","w+") as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanFile)
