def mensaje():
  print("Estamos aprendiendo Python")
  print("Estamos aprendiendo instrucciones basicas")
  print("Poco a poco iremos avansando")
  print("Error 2")

def suma(num1, num2):
  print(num1+num2)

def suma2(num1, num2):
  resultado = num1 + num2
  return resultado

mensaje()
mensaje()
print("Ejecuntando codigo fuera de funcion")
mensaje()
suma(10, 20)
suma(15, 30)

print(suma2(15, 30))

almacena_resultado = suma2(5,8)
print(almacena_resultado)
miLista= ["Carlos","Catherine","Alberto","Granana"]
print(miLista[1])
print(miLista[-2])
print(miLista[0:2])
print(miLista[1:3])
miLista.append("Vasquez")
print(miLista[:])
miLista.insert(2,"Isaza")
print(miLista[:])
miLista.extend(["Sandra","Lucas",5,True, 78.35])
print(miLista[:])
print(miLista.index("Granana"))
print("Granana" in  miLista)
print("Falso" in miLista)
miLista.remove("Granana")
print(miLista[:])
miLista.pop()
print(miLista[:])
miLista2=["Satan","Lucia"]
miLista3= miLista + miLista2
print(miLista3[:])
miLista3 = miLista3 * 3
print(miLista3[:])
miTupla =("Carlos","Granada")
print(miTupla[:])
miLtista4=list(miTupla)
print(miLtista4[:])
print(type(miLtista4))
miLtista4.append("Carlos")
miTupla2=tuple(miLtista4)
print("Carlos" in miTupla2)
print(type(miTupla2))
print(miTupla2.count("Carlos"))
print(len(miTupla2))
miTuplaFecha = ("Juan", 12, 1, 1986)
nambre, dia, mes, agno = miTuplaFecha
print(agno)
print(mes)
print(dia)
print(nambre)
#Dicionarios
miDicionario={"Colombia":"Bogota","Alemania":"Berlin","España":"Madril"}
print(miDicionario["Colombia"])
print(miDicionario)
miDicionario["Italia"]="Lisboa"
print(miDicionario)
miDicionario["Italia"]="Roma"
print(miDicionario)
del miDicionario["Italia"]
print(miDicionario)
miTupla3=["España","Francia","Reino Inido","Alemania"]
miDicionario2={miTupla3[0]:"Madrid",miTupla3[1]:"Paris",miTupla3[2]:"Londres",miTupla3[3]:"Berlin"}
print(miDicionario2)
print(miDicionario2["Francia"])
miDicionario3={23:"Jordan", "Nombre":"Muchael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(miDicionario3[23])
print(miDicionario3["anillos"])
miDicionario4={23:"Jordan", "Nombre":"Muchael", "Equipo":"Chicago", "anillos":{"teampoeadas":[1991,1992,1993,1996,1997,1998]}}
print(miDicionario4["anillos"])
print(type(miDicionario4))
print(miDicionario4.keys())
print(miDicionario4.values())
print(len(miDicionario4))
#Practicas IF
def evaluacion(nota):
  if nota >= 5:
    return "Aprobado"
  else:
    return "No Aprobado"
print("Programa de evaluzacion de notas de alumnos")
notaAlumno = input()
print(evaluacion(4))
print(evaluacion(int(notaAlumno)))
#Mejora de codigo
def evaluacion2(nota):
  valoracion="Aprobado"
  if nota<5:
    valoracion="No aprobado"
  return valoracion
print("Programa de evaluacion de notas de alumnos 2")
notasAlumno2 = input()
print(evaluacion2(int(notasAlumno2)))

print("Verficación de accesos")

edad_usuario=int(input("Introduce tu edad, por favor: "))
if edad_usuario < 18:
  print("No tienes permiso")
elif edad_usuario > 120:
  print("Ya esta muy vuejo para pasar")
else:
  print("Puedes pasar")
print("El programa ha finalizado")

edad=-7
if 0<edad<100:
  print("Edad es correcta")
else:
  print("Edad incorrecta")

salrio_presidente = int(input("Introduce salario presidente: "))
print("Salario presidente: "+ str(salrio_presidente))

salrio_director = int(input("Introduce salario director: "))
print("Salario director: "+ str(salrio_presidente))

salrio_jefe_area = int(input("Introduce salario Jefe Area: "))
print("Salario Jefe Area: "+ str(salrio_director))

salrio_administrativo = int(input("Introduce salario administatico: "))
print("Salario administatico: "+ str(salrio_administrativo))

if salrio_administrativo<salrio_jefe_area<salrio_director<salrio_presidente:
  print("Todo funciona correctamente")
else:
  print("Algo falla en esta empresa")
