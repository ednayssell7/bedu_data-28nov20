#tarea aplicar conocimientos de uso de la funcion map en python

#agregar un descueno aleatorio de entre 5, 10 y 15 % a todos los precios
#imprimir menu sin descuento
#imprimir menu con descuento
#usar random 
import random

precios_en_menu = [1975, 1825, 275, 1500, 850, 675, 1175, 1600, 2175, 2175, 625, 1150, 1175, 350, 1125, 1250, 1875, 1275, 825, 1575, 300, 1275, 875, 1650, 875]


descuento = [5, 10, 15]
descuento_aleatorio = random.choices(descuento)
dividendo = 100
        
def operacion_desc(precio):
    for j in descuento:
        for i in descuento_aleatorio:
            desc_random = i
            descuento_total = precio * (desc_random/dividendo)
            descuento_total = float(descuento_total)
        total = precio - descuento_total
        total = float(total)
        return desc_random

#def operacion_total(precio_1):
    #for j in descuento_total:
       # descuento_total = random.sample(descuento, 1)
      #  Total = precio_1 - descuento_total
     #   Total = float(Total)
    #return Total

 
aleatorio_desc_precios = list(map(operacion_desc, precios_en_menu))    
desc_precios_menu = list(map(operacion_desc, precios_en_menu))

print(f'Precios del menu: {precios_en_menu}')
print(f'Precios con descuento: {desc_precios_menu}')



