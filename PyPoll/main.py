# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:58:26 2017

@author: Felipe
"""
import csv, os

csvpath1 = os.path.join('resources', 'election_data_1.csv')
csvpath2 = os.path.join('resources', 'election_data_2.csv')

candidates = []

with open(csvpath1, 'r') as csvFile1:

    csvReader1 = csv.reader(csvFile1, delimiter=',')

    # Skipp headers
    next(csvReader1, None)
        
    for row in csvReader1:

        if row[2] not in candidates:
            candidates.append(row[2])

with open(csvpath2, 'r') as csvFile1:

    csvReader1 = csv.reader(csvFile1, delimiter=',')

    # Skipp headers
    next(csvReader1, None)
        
    for row in csvReader1:

        if row[2] not in candidates:
            candidates.append(row[2])
            
print (candidates)
