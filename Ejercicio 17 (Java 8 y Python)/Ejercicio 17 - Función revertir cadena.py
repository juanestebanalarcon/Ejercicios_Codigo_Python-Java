cadena_inicial=" "
cadena_inicial=input("Ingrese cadena a revertir: ")
print("scriba una función que reverse una cadena (En cualquier lenguaje) sin usar un método prexistente para esto.")
print()
def revertir_cadena(cadena:str):
    cadena_revertida=" "
    caracter=' '
    for i in cadena_inicial:
        caracter=i 
        cadena_revertida=caracter+cadena_revertida
    return f'La cadena ingresada fue: {cadena_inicial} y el resultado al revertirla es: {cadena_revertida}'
print(revertir_cadena(cadena_inicial))        