import csv

file = open('./employees.csv', 'r')

reader = csv.reader(file)

recodeArray = []
managersCount = 0
totSalary = 0

arrSalary = []
lowSalary = 0


for row in reader:
    
    if (row[2] != 'salary'):
        print(row[2])
        
