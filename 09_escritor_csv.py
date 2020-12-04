#implementacion de escritura en archivos csv
import csv
import random

#definir el nombre de una archivo
filename = 'tmp/archivo_fake.csv'
#especificar columnas
colums = ['id', 'name', 'age']

#TAREA GENERAR UN LISTADO DE IDS USANDO RANDOM Y CADA FUNCION DEBE DE RETORNAR LOS IDS FALSOS

def fake_id(id_fake):
    id_fake = [123, 456, 789, 101, 321, 654, 987, 111, 999, 222]
    id_fake = random.choices(id_fake)
    return id_fake

def fake_name(names_fake):
    names_fake = ['Edna', 'Angel', 'Maria', 'Leticia', 'Denisse', 'Jose', 'Leonardo', 'Samuel', 'Hugo', 'Julieta']
    names_fake = random.choices(names_fake)
    return names_fake

def fake_age(age_fake):
    age_fakes = [12, 28, 70, 4, 2, 35, 50, 30, 27, 59]
    age_fake = random.choices(age_fake)
    return age_fake 

#abrir contexto
with open(filename, mode='w', newline='') as csv_file:
    #crear una variable para escritor
    writer = csv.DictWriter(csv_file, fieldnames=colums)

    writer.writeheader()

    counter = 1
    while counter <= 10:
        writer.writerow({
            'id': fake_id(id_fake),
            'name': fake_name(names_fake),
            'age': fake_age(age_fake)
        })
        counter += 1
