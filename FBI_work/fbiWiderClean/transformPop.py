#!/usr/bin/env python3

import csv

with open('hcsCitiesCounties.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]

cleanRows = rows

for i in range(1,len(rows)):
	pop = rows[i][3:10]
	reports = rows[i][14:-1]
	dnrCount = 0
	zeroCount = 0

	for j in range(0,len(reports)):
		quarter = str(reports[j].strip())
		if quarter == 'DNR':
			dnrCount = dnrCount + 1
		elif quarter == '0':
			zeroCount = zeroCount +1

	#check if 2016 is a "No Data" year
	if (pop[0].strip() == "No Data") or (pop[0].strip() == "Nan"):
		#check if 2015 is a "No Data" year
		if (pop[1].strip() == "No Data") or (pop[1].strip() == "Nan"):
			#check if 2014 is a "No Data" year
			if (pop[2].strip() == "No Data") or (pop[2].strip() == "Nan"): 
				#check if 2013 is a "No Data" year
				if (pop[3].strip() == "No Data") or (pop[3].strip() == "Nan"):
					#check if 2012 is a "No Data" year
					if (pop[4].strip() == "No Data") or (pop[4].strip() == "Nan"):
						#check if 2011 is a "No Data" year
						if (pop[5].strip() == "No Data") or (pop[5].strip() == "Nan"):
							#check if 2010 is a "No Data" year
							if (pop[6].strip() == "No Data") or (pop[6].strip() == "Nan"):
								#there is no data on population in the past 6 years
								popRecent = "No Data"
							else:
								#most recent population info was 2010
								popRecent = pop[6].strip()
						else:
							#most recent population info was 2011
							popRecent = pop[5].strip()
					else:
						#most recent population info was 2012
						popRecent = pop[4].strip()
				else:
					#most recent population info was 2013
					popRecent = pop[3].strip()
			else:
				#most recent population info was 2014
				popRecent = pop[2].strip()
		else:
			#most recent population info was 2015
			popRecent = pop[1].strip()
	else:
		#most recent population info was 2016
		popRecent = pop[0].strip()


	cleanRows[i][10] = str(popRecent)
	cleanRows[i][11] = str(zeroCount)
	cleanRows[i][12] = str(dnrCount)
	cleanRows[i][13] = str(28 - dnrCount - zeroCount)

with open('hcsCitiesCounties_clean.csv','w+') as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanRows)