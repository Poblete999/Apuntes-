

#Bucle infinito:

#edad = 15
#num = 0

#Si el codigo no finaliza en else sera infinito.
#while edad < 18 :
#   print("Eresa menor de edad, no puedes manejar")

#while True:
#   print(num)
#    num=num+2

num = input("Ingrese un número")

num = 0
while num <= 100:
    print(num)
    num+= 2
print("Primer bucle terminado") #print fuera del ciclo.

while num <= 200:
    print(num)
    num+=2
else:
    print("Mi condició es igual o superior a los 200")
print("Segundo bucle terminado!")

while num <= 300:
    print(num)
    num+=2
    if num == 250: #Si se mueve el IF hacia la izquierda no se imprime la condción, porque corta el while (se ejecuta el bucle y despues hay un IF).
        print("Mi condición es igual a 250")
print("Tercer Bucle terminado!\n")  


#Utilizando el BREAK

while num <= 400:
    print(num)
    num+=2
    if num == 350: #Si el IF rompe el ciclo (se mueve hacia la izquierda) break lanzara error porque solo trabaja para WHILE.
        print("Se detiene la ejecución") 
        break
print(num)
print("Cuarto bucle terminado!\n")

#Loop infinito

while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)


#Ciclo FOR (entrara en el PARCIAL 2).
#Impresion de una lista en consola de forma vertical.

for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)
#ESTE CODIGO NO ESTA BIEN OPTIMIZADO.
# i : un auxiliar un incrementador.

#DE FORMA CORRECTA

print("FOR N°2")
newlist = [1,2,3,4,5,6,7,8,9,10]
for i in newlist:
    print(i)

print("FOR N°3")
for i in range(1,11):
    print(i)