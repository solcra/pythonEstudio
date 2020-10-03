print("Programas de becas año 2019")
distancias_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancias_escuela)
numero_hermanos = int(input("Introdusca el numero de hemobos en el centro: "))
print(numero_hermanos)
salario_familiar = int(input("Intruduce salario anual bruto: "))
print(salario_familiar)

if distancias_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
  print("Tiene derecho a beca")
else:
  print("No tienes derecho a beca")

print("Asignaturas optativas año 2020")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabiliddad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()
if asignatura in ("informática gráfica", "prueba de software", "usabilidad y accsibilidad"):
  print("Asignatura elegida " + asignatura)
else:
  print("La asignatura escogida no está contemplada")

for i in [1,2,3]:
  print("Hola")
for i in["Primavera","Verano","Otroño","Inventario"]:
  print(i)

for i in ["Perros", "Gatos", 3]:
  print("Hola", end=" ")
print("")
email=[False, False]
miEmail=input("Introduce tu dirección de email: ")
for i in miEmail:
  if(i=="@"):
    email[0]=True
  if(i=="."):
    email[1]=True
if email[0]==True and email[1]==True:
  print("El correo es correcto")
else:
  print("EL correo no es correcto")
for i in range(5):
  print(i)
for i in range(5):
  print(f"Valor de la variable {i}")
for i in range(5,9):
  print(f"Valor de la variable: {i}")
for i in range(5,50,3):
  print(f"Valor de la variable: {i}")

valido = False
email2 = input("Introdusca tu imail: ")
for i in range(len(email2)):
  if email2[i]=="@":
    valido = True

if valido:
  print("Email correcto")
else:
  print("Email incorrecto")
print("Url curso python https://www.youtube.com/watch?v=UfUM6uzl5SM&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=17")

i=1
while i<=10:
  print(f"Valor de la variable: {i}")
  i+=1
print("Termine el siclo while")
edad=int(input("Ingresa la edad: "))
while edad<0:
  print("Has ingresado una edad negativa. Vuelva a intentarlo")
  edad=int(input("Ingresa nuva mente que no sea negativa: "))
print("Gracias por coloborar. Puedes pasar")
print(f"Edad del aspirante {edad}")

edad2=int(input("Ingresa la edad: "))
while edad2<5 or edad2>100:
  print("Has ingresado una edad meno de 5 o mayor a 100 Vuelva a intentarlo")
  edad2=int(input("Ingresa nuva mente la edad que se mayor a 5 o meno 100: "))
print("Gracias por coloborar. Puedes pasar")
print(f"Edad del aspirante {edad2}")
import math
print("Programa de cálcular raiz cuadrada")
numero=int(input("Ingresa un numero por favor: "))
intentos=0
while numero<0:
  print("No se puede hallar la raíz de un número negativo")
  if intentos == 2:
    print("Has consumido demasiados intentos. El programa ha finalizado")
    break
  numero=int(input("Ingresa un numero por favor positivo: "))
  if numero<0:
    intentos+=1
if intentos<2:
  solucion=math.sqrt(numero)
  print(f"La raíz cuadrada de {numero} es {solucion}")
print("Finalizacion del programa gracias")
for letra in "Python":
  if letra=="h":
      continue
  print(letra)
nombre="Pildoras Informaticas"
contar = 0
for i in nombre:
  if i == " ":
    continue
  contar +=1
print(f"Numero de letras: {contar}")
print(len(nombre))
class MiClass:
  pass # Para implementar más tarde
  print("Carlos")
email3= input("Introdice tu email, por favor: ")
for i in email3:
  if i == "@":
    arroba=True
    break
else:
  arroba=False
print(arroba)

