
#Se solicita:
#a) Eliminar el ultimo elemento de la lista
#b) Agregar en la primera posicion el numero 2
#c) Eliminar los numeros duplicados de la lista
#d) Obtener la media y la mediana de la lista


numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

del(numeros[8])

print(numeros)

numeros.insert(0,2)

print(numeros)

numeros_sin_repetir = []
for item in numeros:
    if item not in numeros_sin_repetir:
        numeros_sin_repetir.append(item)
        
print(numeros_sin_repetir)



