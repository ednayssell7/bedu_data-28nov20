#aplicar conocimientos de la funcion map en python
import random

Numeros = ['3', '148', '74', '71', '4', '83', '95', '20', '61', '10', '69', '67', '23', '164', '97', '67', '144', '200', '38', '90', '200', '162', '6', '180', '65', '71', '90', '182', '16', '132', '182', '108', '90', '196', '48', '2', '158', '88', '39', '39', '54', '80', '89', '3', '90', '170', '88', '71', '142', '45', '81', '194', '36', '39', '30', '33', '38', '44', '134', '43', '12', '52', '170', '162', '192', '83', '18', '176', '120', '28', '86', '188', '51', '11', '96', '13', '198', '34', '66', '23', '200', '62', '194', '91', '51', '26', '152', '186', '86', '38', '46', '66', '83', '66', '40', '2', '20', '12', '91', '53']
Numeros_int =[int(x) for x in Numeros]
print(type(Numeros_int))


#solicitar al usuario un numero menor que 10 y mayor que 0

numero_random = input(f'Hola, selecciona un numero del 1 al 10: ')
numero_random = int(numero_random) #convertir los numeros a entero   

def multiplicacion(numero):
    # Utilizando el numero del usuario, aplicar a todos los elementos de la lista una multiplicacion por el numero del usuario
    num_multi = numero * numero_random
    return num_multi

#convertir numeros pares a true
def num_pares(num_par):
    if num_par % 2 == 0:
        return True
    else:
        return False   
        
multiplicacion_lista = list(map(multiplicacion, Numeros_int))
pares = list(map(num_pares, Numeros_int))
print(f'Multiplicacion de {numero_random} por cada numero de la lista: {multiplicacion_lista}')
print(f'Cada True es un numero par: {pares}')
    

