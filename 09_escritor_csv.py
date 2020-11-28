#implementacion de escritura en archivos csv
import csv

#definir el nombre de una archivo
filename = 'tmp/archivo_fake.csv'
#especificar columnas
colums = ['id', 'name', 'age']

#TAREA GENERAR UN LISTADO DE IDS USANDO RANDOM Y CADA FUNCION DEBE DE RETORNAR LOS IDS FALSOS

def fake_id():
    pass 

def fake_name():
    pass

def fake_age():
    pass

#abrir contexto
with open(filename, mode='w', newline='') as csv_file:
    #crear una variable para escritor
    writer = csv.DictWriter(csv_file, fieldnames=colums)

    writer.writeheader()

    counter = 1
    while counter <= 20:
        writer.writerow({
            'id': fake_id(),
            'name': fake_name(),
            'age': fake_age()
        })
        counter += 1
