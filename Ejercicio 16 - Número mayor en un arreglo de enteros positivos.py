print("Escriba una función que encuentre el entero más grande en un arreglo de enteros positivos (En cualquier lenguaje)")
import time as t 
import random as r 
t.sleep(2)
#Se genera un arreglo con números enteros positivos aleatorios.
arreglo_positivos = r.sample(range(1,5000),80)
def numero_mayor(lista:list):
    mayor=lista[0]
    for i in lista:
        if i > mayor:
            mayor=i
    return f'El número más grande en el arreglo enviado es: {str(mayor)}'
print(numero_mayor(arreglo_positivos))
