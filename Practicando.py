
estudiante = input("ingrese el nombre del estudiante")
asignatura = input("ingrese el nombre de la asignatura")
nota1 = float(input("ingrese la nota del laboratorio 1"))
nota2 = float(input("ingrese la nota del laboratorio 2"))

promedio = (nota1 * 0.3) + (nota2 * 0.7)

dic = {
    "Nombre del estudiante": estudiante,
    "Nombre de la asignatura": asignatura,
    "Nota 1": nota1,
    "Nota 2": nota2,
    "Promedio": round(promedio, 1)
}

print(dic)

 