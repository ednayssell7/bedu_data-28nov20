#tarea aplicar conocimientos de uso de la funcion map en python

#agregar un descueno aleatorio de entre 5, 10 y 15 % a todos los precios
#imprimir menu sin descuento
#imprimir menu con descuento
#usar random 
import random

precios_en_menu = [1975, 1825, 275, 1500, 850, 675, 1175, 1600, 2175, 2175, 625, 1150, 1175, 350, 1125, 1250, 1875, 1275, 825, 1575, 300, 1275, 875, 1650, 875]

descuento = [0.5, 0.10, 0.15]
        
def operacion_desc(precio):
    desc_random = random.choice(descuento)
    descuento_total = precio * (desc_random)
    total = precio - descuento_total
    return total, descuento_total, desc_random

aleatorio_desc_precios = list(map(operacion_desc, precios_en_menu))    

print(f'Precios del menu: {precios_en_menu}')
print(f'Precios con descuento: {aleatorio_desc_precios}')



