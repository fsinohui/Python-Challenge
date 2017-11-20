# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:17:24 2017

@author: FSinohui
"""

"""Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total amount of revenue gained over the entire period
The average change in revenue between months over the entire period
The greatest increase in revenue (date and amount) over the entire period
The greatest decrease in revenue (date and amount) over the entire period


As an example, your analysis should look similar to the one below:"""
'''
import pandas as pd
url = 'http://usc.bootcampcontent.com/usc-boot-camp/USCLOS201710DATA5-Class-Repository-DATA/Python/Homework Instructions/PyBank/raw_data/budget_data_2.csv'
df = pd.read_csv(url,index_col=0,parse_dates=[0])

for row in df:
    print(row)'''
    
import os
import csv
import pandas as pd


''' 
os.chdir('C:/Users/FSinohui/desktop/moocs/python/gitPython/Python-Challenge/PyBank')
cwd = os.getcwd()
print(cwd)'''



# Set path for file
budget_data_1_csv = os.path.join( "budget_data_1.csv")
budget_data_2_csv = os.path.join( "budget_data_1.csv")

months = 0
revenue = 0
revenueS = 0
revenueE = 0
greatestGain = 0
greatestLoss = 0

with open(budget_data_1_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    rows = [csvheader] + [[row[0],int(row[1])] for row in csvreader]
    
    
    
    for row in rows:
        #revenue = revenue + row[1]
        if row[1] != 'Revenue':  
            revenue = revenue +row[1]
            months = months +1
            
pdcsv1 = pd.read_csv(budget_data_1_csv, nrows = 1)
print(pdcsv1.head(1))
print(pdcsv1.tail(22))

print('Total Months: ', months)       
print('Total Revenue: ',str(revenue))

        
        
        
        