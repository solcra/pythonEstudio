def funcion_decoradora(funcion_parametro):
  def funcion_interio():
    #Acciones adicionales que decoran
    print("Vamos a realizar un cálculo: ")
    funcion_parametro()
    #Acciones adicionales que decoran
    print("Hemos terminado el cálcilo")
  return funcion_interio


@funcion_decoradora
def suma():
  print(15+12)

@funcion_decoradora
def resta():
  print(30-10)

suma()
resta()

def funcion_decoradoraParametro(funcion_parametro):
  def funcion_interio(*args):
    #Acciones adicionales que decoran
    print("Vamos a realizar un cálculo con parametro: ")
    funcion_parametro(*args)
    #Acciones adicionales que decoran
    print("Hemos terminado el cálcilo con parametro")
  return funcion_interio

@funcion_decoradoraParametro
def suma2(num1, num2):
  print(num1+num2)

@funcion_decoradoraParametro
def resta2(num1, num2):
  print(num1-num2)


suma2(23,90)
resta2(10,5)
