
#Funciones

#Caracteristicas:

'''
Argumentos: Pueden aceptar cero o
más argumentos. Estos
argumentos son valores
de entrada que se pasan a
la función al llamarla.
Pueden ser utilizados
dentro de la función para
realizar operaciones
'''
'''
Invocada: La función puede ser
llamada desde cualquier
parte del programa en
cualquier momento,
favoreciendo la reutilización
de código y evitando las
tareas repetitivas.

'''
'''
Ambitos de variables(locales y locales): Las variables definidas dentro de una
función tienen un ámbito local, es decir,
solo son accesibles desde dentro de la
función. Las variables definidas fuera de
una función tienen un ámbito global y
pueden ser accedidas tanto desde
dentro como desde fuera de la función
'''

#Principios de las funciones:

'''
-Reusabilidad:El principio indica que cuando tengamos un fragmento de
código que se utiliza en varios lugares, la mejor opción
sería convertirlo en una función. De esta manera,
evitaremos la repetición de código y facilitaremos la tarea
de modificarlo, ya que solo será necesario realizar cambios
en la función en un único lugar.
-Modularidad:Este principio sostiene que en lugar de escribir extensos
trozos de código, es mejor crear módulos o funciones que
agrupen fragmentos específicos de código acorde a su
funcionalidad. De esta manera, el código se vuelve más
legible y organizado, facilitando su comprensión y
mantenimiento.
'''

#Las funciones sirven para encampsular un codigo en especifico para un ejercicio en especifico.

#Palabra reservada Nombre_de_la_función ():
def mi_primera_funcion():
    print("Esta es mi primera función")


#Se llama a la función

#mi_primera_funcion()

#Se imprime el print

#Es recomendable usar funciones cuando se necesita usar mucho codigo(ayuda a ahorrar codigo).

#Utilizando listas:

def concatenar(lista1, lista2):
    return lista1 + lista2


lista1 = [1,2,3]
lista2 = [4,5,6]

#Las listas se declaran fuera del Scope local (entorno). Aqui no es necesario ubicar los PARAMETROS y/o argumentos antes de la función.

#concatenar() #Si se escribe asi no arrojara nada porque no tiene parametros dentro del parentesis.
print(concatenar(lista1, lista2))

#Utilizando multiplicación:

def multiplicación(num1, num2):
    return num1*num2

#multiplicación() #Si se escribe asi no arrojara nada porque no tiene parametros dentro del parentesis.
print(multiplicación(10,9))

#Ejemplo de una función:

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Se llama a la función suma

resultado=suma(a,b)
print("La suma es de:", resultado)

resultado2=resta(a,b)
print("La resta es de:", resultado2)



