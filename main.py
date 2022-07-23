##Escribir un programa que reciba una cadena de caracteres y
##devuelva un diccionario con cada palabra que contiene y su frecuencia.
##Escribir otra función que reciba el diccionario generado con la función
##anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def dic_frec(cadena:str):
    cadena_separada=cadena.split()
    nuevo_dict = {}

    for i in cadena_separada:
        frecuencia = cadena_separada.count(i)

        nuevo_dict[i]= frecuencia
    return (nuevo_dict)

def palabra_repetida(diccionario):
    frecuencia = 0

    for i in diccionario:
        if diccionario[i]>frecuencia:
            frecuencia = diccionario[i]
            palabra = i

    tupla_frecuencia = (palabra, frecuencia)
    return(tupla_frecuencia)

a = dic_frec("hola hola como como como estas estas tu")

print(a)
print(palabra_repetida(a))
