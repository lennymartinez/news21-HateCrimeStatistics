import matplotlib  
matplotlib.use('TkAgg')   
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('fbiMain_population.csv', newline='', encoding='utf-8') as f:
	reader = csv.reader(f)
	rows = [row for row in reader]
print("we have "+str(len(rows))+" rows")

population = []
for i in range(1,len(rows)):
	population.append(rows[i][2])