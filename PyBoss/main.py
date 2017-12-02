# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:41:34 2017

@author: Rayzel
"""

#pyBoss

import csv, os 


us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath1 = os.path.join('resources', 'employee_data1.csv')
csvpath2 = os.path.join('resources', 'employee_data2.csv')

# Create New HR file
csvpathNew = os.path.join('resources', 'employee_data_new.csv')


empID = []
first = []
last = []
dob = []
ssn = []
state = []
    
# Run the first file
with open(csvpath1, 'r') as csvFile1:

    csvReader1 = csv.reader(csvFile1, delimiter=',')

    # Skipp headers
    next(csvReader1, None)
        
    for row in csvReader1:

        # Append data from the row
        empID.append(row[0])
        
        firstname = row[1].split()[0]
        lastname = row[1].split()[1]
        first.append(firstname)
        last.append(lastname)
        
        #dateformate = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
        #dob.append(dateformate)
        dob.append(row[2])
        
        num = '***-**-', row[3][-4:]
        ssn.append(num)
        
        state.append(us_state_abbrev[row[4]])
        
# Run the second file        
with open(csvpath2, 'r') as csvFile2:

    csvReader2 = csv.reader(csvFile2, delimiter=',')

    # Skipp headers
    next(csvReader2, None)
        
    for row in csvReader2:

        # Append data from the row
        empID.append(row[0])
        
        firstname = row[1].split()[0]
        lastname = row[1].split()[1]
        first.append(firstname)
        last.append(lastname)
        
        #dateformate = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
        #dob.append(dateformate)
        dob.append(row[2])
        
        num = '***-**-', row[3][-4:])
        ssn.append(num)
        
        state.append(us_state_abbrev[row[4]])


    # Zip lists together
    cleanCSV = zip(empID, first, last, dob, ssn, state)

    with open(csvpathNew, 'w', newline="") as csvFile:

        csvWriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvWriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])

        # Write the zipped lists to a csv
        csvWriter.writerows(cleanCSV)

