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