#usando la funcion filter de python

#funciones

def numero_par(numero):
    if numero % 2 == 0:
        #if numero % 2 =! 0 para los numeros nones
        return True

#ejecucion
numeros = [3, 148, 74, 71, 4, 83, 95, 20, 61, 10, 69, 67, 23, 164, 97, 67, 144, 200, 38, 90, 200, 162, 6, 180, 65, 71, 90, 182, 16, 132, 182, 108, 90, 196, 48, 2, 158, 88, 39, 39, 54, 80, 89, 3, 90, 170, 88, 71, 142, 45, 81, 194, 36, 39, 30, 33, 38, 44, 134, 43, 12, 52, 170, 162, 192, 83, 18, 176, 120, 28, 86, 188, 51, 11, 96, 13, 198, 34, 66, 23, 200, 62, 194, 91, 51, 26, 152, 186, 86, 38, 46, 66, 83, 66, 40, 2, 20, 12, 91, 53]

numeros_pares = list(filter(numero_par, numeros))
numeros_pares.sort() #(reverse=True) de mayor a menor
print(numeros_pares)

#crear lista de numeros mayores a 100 y cuantos son
#crear lista de numeros menores a 100 y cuantos son
def numero_mayor_100(numero):
    if numero >= 100:
        return True

def numero_menor_100(numero):
    if numero <= 100:
        return True

numero_mayor_100 = list(filter(numero_mayor_100, numeros))
print(numero_mayor_100)
print(len(numero_mayor_100))

numero_menor_100 = list(filter(numero_menor_100, numeros))
print(numero_menor_100)
print(len(numero_menor_100))

#filter numeros pares mayores a 100
numero_mayor_100 = list(filter(numero_mayor_100, numeros_pares))
numero_mayor_100.sort()
print(numero_mayor_100)
print(len(numero_mayor_100))
