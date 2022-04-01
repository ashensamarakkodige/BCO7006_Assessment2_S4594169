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
lowSalaryFName = lowSalaryHolder[0][0]
lowSalaryLName = lowSalaryHolder[0][1]       




text1 = 'The average salary of managers is ' + str(totSalary/managersCount) + ' dollars.'
text2 = str(lowSalaryFName)+' '+str(lowSalaryLName)+' has the lowest salary ($' + str(lowSalary) +')'

print(text1)
print(text2)
        