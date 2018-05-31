import csv
import math

with open('hcsCitiesCounties_short.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]

cleanRows = rows
triClass = [0,0,0]
# for i in range(1,len(rows)):
# 	pop = rows[i][3]
# 	outputCounter = [-1,-1,-1]

# 	#counters: zero, dnr, report
# 	triCounter = [rows[i][4], rows[i][5], rows[i][6]]
# 	for counter in triCounter:
# 		if (counter >= 0 ) or (counter < 4):

for i in range(1, len(rows)):
	print(i)
	#counters: zero, dnr, report
	triCounter = [rows[i][4], rows[i][5], rows[i][6]]
	for count in triCounter:
		counter = int(count.strip())
		k = triCounter.index(count)
		if (counter >= 0) and (counter < 4):
			triClass[k] = 0
		elif (counter >= 4) and (counter < 8):
			triClass[k] = 1
		elif (counter >= 8) and (counter < 12):
			triClass[k] = 2
		elif (counter >= 12) and (counter < 16):
			triClass[k] = 3
		elif (counter >= 16) and (counter < 20):
			triClass[k] = 4
		elif (counter >= 20) and (counter < 24):
			triClass[k] = 5
		elif (counter >= 24) and (counter < 28):
			triClass[k] = 6
		else:
			triClass[k] = 7
	pop = rows[i][3]
	if pop == 'No Data':
		cleanRows[i][10] = "-1"
	elif pop == '0':
		cleanRows[-1][10] = "0"
	else:
		a = str(math.log10(float(pop)))
		cleanRows[i][10] = a[0]


	cleanRows[i][7] = str(triClass[0])
	cleanRows[i][8] = str(triClass[1])
	cleanRows[i][9] = str(triClass[2])


with open('hcsPriorities.csv','w+') as f:
			csvWriter = csv.writer(f,delimiter=',')
			csvWriter.writerows(cleanRows)