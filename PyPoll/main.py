# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 23:58:26 2017

@author: Felipe
"""
import csv, os

csvpath1 = os.path.join('resources', 'election_data_1.csv')
csvpath2 = os.path.join('resources', 'election_data_2.csv')

candidates = {}
votes = 0

with open(csvpath1, 'r') as csvFile1:

    csvReader1 = csv.reader(csvFile1, delimiter=',')

    # Skipp headers
    next(csvReader1, None)
        
    for row in csvReader1:
        
        votes = votes+1
        
        key = row[2]
        
        if key in candidates:
            candidates[key] = candidates[key] + 1
        else:
            candidates[key] = 1
            
            
with open(csvpath2, 'r') as csvFile1:

    csvReader1 = csv.reader(csvFile1, delimiter=',')

    # Skipp headers
    next(csvReader1, None)
        
    for row in csvReader1:
        
        votes = votes+1
        
        key = row[2]
        
        if key in candidates:
            candidates[key] = candidates[key] + 1
        else:
            candidates[key] = 1

print('Election Results')
print('-----------------')
print('Total Votes: ',votes)
print('-----------------')
highest = 0
for candidate in candidates:
    print (candidate, ': ', str(round(float(candidates[candidate]/votes),2)*100),'% (',candidates[candidate],')')
    if candidates[candidate] > highest:
        highest = candidates[candidate]
        winner = candidate
print('-----------------')
print('Winner:', winner)
print('-----------------')
