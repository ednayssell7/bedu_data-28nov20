#implementacion de escritura en archivos csv
import csv
import random

#definir el nombre de una archivo
filename = 'tmp/archivo_fake_tarea.csv'
#especificar columnas
colums = ['id', 'name', 'age']

#TAREA GENERAR UN LISTADO DE IDS USANDO RANDOM Y CADA FUNCION DEBE DE RETORNAR LOS IDS FALSOS

id_fake = [123, 456, 789, 101, 321, 654, 987, 111, 999, 222]
names_fake = ['Edna', 'Angel', 'Maria', 'Leticia', 'Denisse', 'Jose', 'Leonardo', 'Samuel', 'Hugo', 'Julieta']
age_fakes = [12, 28, 70, 4, 2, 35, 50, 30, 27, 59]


def fake_id(id_fake):
    id_fake = random.choices(id_fake)
    return id_fake

def fake_name(names_fake):
    names_fake = random.choices(names_fake)
    return names_fake

def fake_age(age_fake):
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
            'id': fake_id(),
            'name': fake_name(),
            'age': fake_age()
        })
        counter += 1
