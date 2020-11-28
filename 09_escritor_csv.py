#implementacion de escritura en archivos csv
import csv

#definir el nombre de una archivo
filename = 'tmp/archivo_fake.csv'
#especificar columnas
colums = ['id', 'name', 'age']

#abrir contexto
with open(filename, mode='w', newline='') as csv_file:
    #crear una variable para escritor
    writer = csv.DictWriter(csv_file, fieldnames=colums)

    writer.writeheader()

    counter = 1
    while counter <= 20:
        writer.writerow({
            'id': counter * 123,
            'name': f'Dalai {counter} {counter * 123}',
            'age': f'{counter * 5}'
        })
        counter += 1
