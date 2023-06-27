
#Tipos de datos en python:

#Datos primitivos, poseen estructuras complejas.

#Enteros/int/55
#Punto flotante (de alta presición)/float/2.9
#Caracteres/Str/HolaMundo
#Booleno/boolean/Falso,Verdadero
#Complejo/complex/2 + 4X


peso = 70
estatura = 1.75

IMC = peso/(estatura**2)

print ("Mi IMC es de: {:.5f}".format(IMC), "\n")

asignatura = "programación"

print("La asignatura de:", asignatura, "es de: ",len(asignatura))
len(cuenta la cantidad de caracteres)

Booleano: (tipo de dato)
(Dos valores verdadero y falto.)
ampolleta = False
interruptor = True

print(type("indica_el_tipo_de_dato_con_el_que_estamos_trabajando"))
(Cualquier valor se puede transformar a booleano)
print (bool("valor que se quiere transformar"))

#Tipo Listas (permite almacenar en elementos)
#Como se inicializa
 
(Con [corchetes] o con la palabra reservada list)
len("Cuenta la cantidad de elementos en la lista")


estudiantes = list[Juan, Joel, Maria, Patricio]
números = list[1,2,3,4]
lenguaje = list["Python"]

#Concatenar

print list("")
print (list (range()))


lent:(Cuenta los elementos)
count:(analiza la concurrencia de un elemento)

#Si tengo 10 elementos y quiero imprimir 1 se usa index, que es la posición del elemento (no el valor).
#Se utiliza la ubicación del elemento, las posiciones comienzan a partir del 0 de izquierda a derecha,
#truco para ubicar un elemento: usar números negativos la cuenta es al reves (de derecha a izquierda)

#Consultar la posición del dato

print(index("elemento"))

#TUPLAS
#Las listas se pueden modificar pero las tuplas no, son inmutables!

tuple = (1, 2, 3)
#tupla[0] = 5 # Error! TypeError
#Si se quiere modificar una tupla se tiene que transformar en una lista, pero es tonto porque se puede crear
#la lista desde el principio.

tupla = (1, 2, 3, 5)
tupla = list[1, 2, 4, 5]


#Las Tuplas son más eficientes que las listas.
#Como genero tuplas?

newtuple = tupla(1,2,3,4)
tupla = (1, 2, 3, 4, 5)
#O
tupla = 1, 2, 3, 4, 5 
print(tupla) #1, 2, 3, 4, 5
print(type(tupla)) 
#La tupla puede tener una lista dentro
list = [(1, 2, 3, true)]
#OPERANDO CON TUPLAS

#Se puede transformar una lista en una tupla:

lista = [1, 2, 3]
tupla = tupla(lista)

#Trozo de una tupla.


#SETs {}
"Inicializar sets"
palabra_reservada = set

conjunto_vacio = set{}
#O llaves
conjunto_vacio1 = {}
print(type(conjunto_vacio1))

conjunto_de_colores = set({"Azul","Rojo", "Verde", "Azul"})
#O
conjunto_de_animales = set{"Vaca", "Gato", "Perro"}

print(type(conjunto_de_colores))

#Añadir elemento al set

conjunto_de_colores.add("Amarillo")


#En los sets no se puede acceder la posición del elemento, porque se guarda de una forma distinta.
#En los sets no se pueden duplicar los elementos.

#DICCIONARIOS 
palabra_reservada = dict{}
#Ejemplo

datos_personales = {"Nombre": "Benjamín",
                    "Institución": "Ulagos",
                    "Edad":18,
                    "Asignaturas":{"Estructura de datos","Programación"}}
#Los elementos de la izquierda son claves y los de la derecha son valores. JUNTOS SON UN ELEMENTO.
#Como accedemos a la información dentro del diccionario?



#Como agregamos una nueva clave al diccionario?
datos_personales["Ciudad"] = "Osorno"
#Como eliminar una clave del diccionario?
del["Ciudad"]