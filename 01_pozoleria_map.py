#como usar la funcion map de python

IVA = 0.16 

def aplicar_iva(precio):
    resultado = precio * (1 + IVA)
    return round(resultado, 2)

Precios_sin_iva = [415, 90, 355, 115, 100, 250, 600]
print(Precios_sin_iva)

#usar map para aplicar una funcion a cada elemento de mi lista

precios_con_iva = list(map(aplicar_iva, Precios_sin_iva))

print(precios_con_iva)
