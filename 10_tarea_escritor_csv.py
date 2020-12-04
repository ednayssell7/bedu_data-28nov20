#implementacion de escritura en archivos csv
import csv
import random

#definir el nombre de una archivo
filename = 'tmp/archivo_fake_tarea.csv'
#especificar columnas
colums = ['id', 'name', 'age']

#TAREA GENERAR UN LISTADO DE IDS USANDO RANDOM Y CADA FUNCION DEBE DE RETORNAR LOS IDS FALSOS

id_fake_ = [123, 456, 789, 101, 321, 654, 987, 111, 999, 222]
name_fake = ['Edna', 'Angel', 'Maria', 'Leticia', 'Denisse', 'Jose', 'Leonardo', 'Samuel', 'Hugo', 'Julieta']
age_fake = [12, 28, 70, 4, 2, 35, 50, 30, 27, 59]


def fake_id(idfake):
    random_id = random.choice(id_fake_)
    return random_id

def fake_name(namesfake):
    random_names = random.choice(name_fake)
    return random_names

def fake_age(agefake):
    random_age= random.choice(age_fake)
    return random_age

randomID = random.choice(list(map(fake_id, id_fake_)))
randomName = random.choice(list(map(fake_name, name_fake)))
randomAge = random.choice(list(map(fake_age, age_fake)))

#abrir contexto
with open(filename, mode='w', newline='') as csv_file:
    #writer = csv.DicWriter(file, delimiter='|')
    #crear una variable para escritor
    writer = csv.DictWriter(csv_file, fieldnames=colums)

    writer.writeheader()

    counter = 1
    while counter <= 10:
        writer.writerow({
            'id': randomID,
            'name': randomName,  
            'age': randomAge
        })
        counter += 1