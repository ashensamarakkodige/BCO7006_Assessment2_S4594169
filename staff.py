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
        
        recodeArray.append(row)
        arrSalary.append(float(row[2]))
        lowSalary = min(arrSalary)
        
        if(row[3] == 'Manager'):

            totSalary += float(row[2])
            managersCount += 1


lowSalaryHolder = list(filter(lambda c: float(c[2]) == lowSalary, recodeArray))         
print(lowSalaryHolder) 


text1 = 'The average salary of managers is ' + str(totSalary/managersCount) + ' dollars.'


print(text1)
        