import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('fbiMain_v2.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]
print("we have "+str(len(rows)-1)+" rows")

population = []
dnr = []
zero = []
for i in range(1,len(rows)):
	population.append(int(rows[i][2]))
	dnr.append(int(rows[i][3]))
	zero.append(int(rows[i][4]))

print("Population")
print("average: ", np.average(population))
print("variance: ", np.var(population))
print("---")
print("DNR quarters")
print("average: ", np.average(dnr))
print("variance: ", np.var(dnr))
print("---")
print("Zero quarters")
print("average: ", np.average(zero))
print("variance: ", np.var(zero))

hist, binEdges = np.histogram(population, bins=[0,100,1000,10000,100000,1000000])
print(hist)
print(binEdges)