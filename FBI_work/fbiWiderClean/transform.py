#!/usr/bin/env python3

import csv
from itertools import groupby

with open('hcsCitiesAndCounties.csv') as f:
    # dict reader makes each row a dict
    reader = csv.DictReader(f)

    # list comprehension iterates through the reader
    # and creates a list of dicts
    rows = [row for row in reader]

output_rows = []

# groupby takes a sorted iterable (list)
# keyfunc is just telling it what to sort and group by
def keyfunc(x): return x['agencyName']
for city, group in groupby(sorted(rows, key=keyfunc), key=keyfunc):
    
    group = list(group) # group is an iterable, converting to list

    # starting the base of the output row, we will add more things to it
    output_row = {
        'agencyName': city,
        'agencyType': group[0]['agencyType'],
        'state': group[0]['state'],
    }

    # in order to differentiate between no data vs missing years, we create this dict
    group_dict = {int(x['year']):x for x in group}

    # loop through each year, inclusive (that's why there's a +1)
    for year in range(2010, 2016+1):
        row = group_dict.get(year, {}) # if no row for year, return empty dict

        # if no data, explicitly write it out
        output_row[f'{year}q1'] = row.get('q01', 'No Data')
        output_row[f'{year}q2'] = row.get('q02', 'No Data')
        output_row[f'{year}q3'] = row.get('q03', 'No Data')
        output_row[f'{year}q4'] = row.get('q04', 'No Data')
        output_row[f'{year}_population'] = row.get('population', 'No Data')

    output_rows.append(output_row)

with open('output.csv', 'w') as f:
    # get fieldnames (headers) from the first output row dict
    writer = csv.DictWriter(f, fieldnames=output_rows[0].keys())
    writer.writeheader()
    writer.writerows(output_rows)
