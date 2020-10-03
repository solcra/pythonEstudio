def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplica(num1, num2):
  return num1 * num2

def divicion(num1, num2):
  try:
    return num1 / num2
  except ZeroDivisionError:
    print("No se puede dividir entre 0")
    return "Operacion erronea"

obc1 = None
obc2 = None
while True:
  try:
    if obc1 != None:
      obc1 = obc1
    else:
      obc1 = (int(input("Inserte el primer numero: ")))
    if obc2 != None:
      obc2 = obc2
    else:
      obc2 = (int(input("Ingresa el segundo numero: ")))
    break
  except ValueError:
    print("Los valores introducidos no son correctos intentalo nueva mente")
  

operacion = input("Ingresa la operacion (suma, resta, multiplica, divide): ")
  
if operacion == "suma":
  print(suma(obc1, obc2))
elif operacion == "resta":
  print(resta(obc1, obc2))
elif operacion == "multiplica":
  print(multiplica(obc1, obc2))
elif operacion == "divide":
  print(divicion(obc1, obc2))
else:
  print("Operacion no comtemplada")
print("Oprecion ejecutada. Contunyacuib de ejecucion del programa")

def dividir2():
  try:
    opc1=(float(input("Ingresa primer numero: ")))
    opc2=(float(input("Ingresa segundo numero: ")))
    print(f"La divicion es: {opc1/opc2}")
  except ValueError:
    print("El valor introducido es erróneo")
  except ZeroDivisionError:
    print("No se puede dividir entre 0!")
  finally:
    print("Cálculo finalizado")
dividir2()


def evaluaEdad(edad):
  if edad < 0:
    raise TypeError("No se permiten edades negativas")
  if edad < 20:
    return "eres muy joven "
  if edad < 40:
    return "eres joven"
  if edad < 65:
    return "Eres maduro"
  if edad < 100:
    return "Cuidate"
print(evaluaEdad(19))
print(evaluaEdad(20))
print(evaluaEdad(65))
print(evaluaEdad(100))
#print(evaluaEdad(-15))

import math

def calculaRaiz(num1):
  if num1<0:
    raise ValueError ("El numero no puede ser negativo")
  else:
    return math.sqrt(num1)
op1=(int(input("Introduce un número: ")))
while True:
  try:
    print(calculaRaiz(op1))
    break
  except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
    op1=(int(input("Intenta nueva mente introduce un número: ")))

  
print("Programa terminado")

