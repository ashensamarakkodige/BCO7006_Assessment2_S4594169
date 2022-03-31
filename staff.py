import csv

file = open('./employees.csv', 'r')

reader = csv.reader(file)

print(reader)