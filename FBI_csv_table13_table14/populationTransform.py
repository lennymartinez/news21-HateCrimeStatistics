import csv

with open('fbiMain_population.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)

	rows = [row for row in reader]

cleanRows = rows

for i in range(1,len(rows)):
	reports = rows[i][10:-2]
	dnrCount = 0
	zeroCount = 0
	for j in range(0,len(reports)):
		quarter = str(reports[j].strip())
		if quarter == 'DNR':
			dnrCount = dnrCount + 1
		elif quarter == '0':
			zeroCount = zeroCount +1

	cleanRows[i][-2] = dnrCount
	cleanRows[i][-1] = zeroCount


#Getting latest population info
for i in range (1, len(rows)):
	#first we'll get the population values from years 2010 to 2016 as a list
	pop = rows[i][2:9]


	#check if 2016 is a "No Data" year
	if pop[6].strip() == "No Data":
		#check if 2015 is a "No Data" year
		if pop[5].strip() == "No Data":
			#check if 2014 is a "No Data" year
			if pop[4].strip() == "No Data": 
				#check if 2013 is a "No Data" year
				if pop[3].strip() == "No Data":
					#check if 2012 is a "No Data" year
					if pop[2].strip() == "No Data":
						#check if 2011 is a "No Data" year
						if pop[1].strip() == "No Data":
							#check if 2010 is a "No Data" year
							if pop[0].strip() == "No Data":
								#there is no data on population in the past 6 years
								populationRecent = "No Data"
							else:
								#most recent population info was 2010
								populationRecent = pop[0].strip()
						else:
							#most recent population info was 2011
							populationRecent = pop[1].strip()
					else:
						#most recent population info was 2012
						populationRecent = pop[2].strip()
				else:
						#most recent population info was 2013
						populationRecent = pop[3].strip()
			else:
				#most recent population info was 2014
				populationRecent = pop[4].strip()
		else:
			#most recent population info was 2015
			populationRecent = pop[5].strip()
	else:
		#most recent population info was 2016
		populationRecent = pop[6].strip()


	cleanRows[i][9] = str(populationRecent)





with open('fbiMain_population2.csv','w+') as my_csv:
			csvWriter = csv.writer(my_csv,delimiter=',')
			csvWriter.writerows(cleanRows)