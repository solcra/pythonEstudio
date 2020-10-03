def numero_par(num):
  if num % 2 ==0:
    return True



numeros=[17,24,7,39,8,51,92]

print(list(filter(numero_par,numeros)))

print("Prueba dos")
print(list(filter(lambda numero_par2: numero_par2%2==0,numeros)))


class empleado:
  def __init__(self, nombre, cargo, salario):
    self.nombre = nombre
    self.cargo = cargo
    self.salario= salario
  def __str__(self):
    return f"{self.nombre} que trabajo como {self.cargo} tiene un salario de $ {self.salario}"

listaEmpleados=[
  empleado("Juan","Director", 750000),
  empleado("Andrea","Precidente", 850000),
  empleado("Antonio","Administrativo", 25000),
  empleado("Sara","Secretaria", 27000),
  empleado("Mario","Batones", 21000)
]
salario_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados)

for empleado_salario in salario_altos:
  print(empleado_salario)