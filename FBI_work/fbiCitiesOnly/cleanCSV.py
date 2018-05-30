import csv

with open('fbiMain.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)

	rows = [row for row in reader]

cleanRows = rows
i = 3

for i in range(1,len(rows)):
	agencyname = rows[i][2]
	endchr = agencyname[-1]
	if (endchr == "2") or (endchr == "3"):
		cleanRows[i][2] = agencyname[:-1]

with open("fbiMain_cleaned.csv","w+") as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanRows)
