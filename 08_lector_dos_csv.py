
#utilizando modulo csv para lectura de archivos csv
import csv

filename = 'employees.csv'

with open(filename, mode='r') as csv_file:
    #csv file converter into a dictionari
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row)
        #print(row['Name']) not ideal
        #every dictionary has .get method
        s = row.get('Salary')
        n = row.get('Name')
        print(f'{n} earns {s}')
