# Implementacion de escritura en archivos csv
import csv

filename = 'tmp/archivo_fake.csv'
columns = ['id', 'name', 'age']

with open(filename, mode='w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=columns)

    writer.writeheader()

    counter = 1
    while counter <= 20:
        writer.writerow({
            'id': counter * 12123,
            'name': f'Dalai {counter} {counter * 234}',
            'age': f'{counter * 5}'
        })
        counter += 1