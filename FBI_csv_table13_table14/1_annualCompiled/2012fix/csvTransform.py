import csv


with open('Table13_2012.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)

	rows = [row for row in reader]


cleanRows = rows

#let's go row by row
for i in range(1,len(cleanRows)):
	#then check the columns
	for j in range(0,9):
		#once we have a row and column cell, we check if it's empty
		if rows[i][j].strip() == '':
			#empty column is state (0) or agencyType (1)
			if (j == 0) or (j == 1):
				#replace rule with above cell
				cleanRows[i][j] = rows[i-1][j]
			#empty column is agencyName (2)
			elif (j == 2):
				#if it's empty, we mark it for deletion
				cleanRows[i][j] = '@@Delete Me@@'
			#empty column is a quarter (3 -> q1, 4 -> q2, 5 -> q3, 6 -> q4)
			elif (j == 3) or (j == 4) or (j == 5) or (j ==6):
				#empty column means they did not report, so we note that.
				cleanRows[i][j] = 'DNR'
			#empty column is population column
			elif (j == 7):
				#if we have no population, we mark the cell 
				cleanRows[i][j] = 'Not Available'
			#empty column is addendum colum
			elif (j == 8):
				#means that column is not part of addendum
				cleanRows[i][j] = '0'

#loop through addendum column one more time to change actual files to '1'
for i in range(1,len(cleanRows)):
	if rows[i][8].strip() == 'Addendum':
		cleanRows[i][8] = '1'


	# #check state
	# if rows[i][0].strip() == '':
	# 	cleanRows[i][0] = rows[i-1][0]

	# #check agencyType
	# if rows[i][1].strip() == '':
	# 	cleanRows[i][1] = rows[i-1][1]

	# #check agencyName
	# if rows[i][2].strip() == '':
	# 	cleanRows[i][2] = '@@Delete Me@@'

	# #check quarters
	# if rows[i][3].strip() == '':
	# 	cleanRows[i][3] = 'DNR'

	# if rows[i][3].strip() == '':
	# 	cleanRows[i][3] = 'DNR'

	# if rows[i][3].strip() == '':
	# 	cleanRows[i][3] = 'DNR'	
	


cleanRows[0] = ['state', 'agencyType', 'agencyName', 'q01', 'q02', 'q03', 'q04', 'population','addendum']

with open('t13_2012_1.csv','w+') as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanRows)
