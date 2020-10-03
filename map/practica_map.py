class empleado:
  def __init__(self, nombre, cargo, salario):
    self.nombre = nombre
    self.cargo = cargo
    self.salario= salario
  def __str__(self):
    return f"{self.nombre} que trabajo como {self.cargo} tiene un salario de $ {self.salario}"

listaEmpleados=[
  empleado("Juan","Director", 6700),
  empleado("Andrea","Precidente", 7500),
  empleado("Antonio","Administrativo", 2100),
  empleado("Sara","Secretaria", 2150),
  empleado("Mario","Batones", 1800)
]

def calculo_comicion(empleado):
  if(empleado.salario<=3000):
    empleado.salario = empleado.salario*1.03
  return empleado

listaEmpleadosComicion=map(calculo_comicion, listaEmpleados)

for empleado_salario in listaEmpleadosComicion:
  print(empleado_salario)