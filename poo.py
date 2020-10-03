class Coche():

  #constructor
  def __init__(self):
    self.largoChasis=250
    self.anchoChasis=120
    #En camsular no sera asesible por fuera de la clase
    self.__ruedas=4
    self.enmarcha=False
  #propiedades
  """
  largoChasis=250
  anchoChasis=120
  ruedas=4
  enmarcha=False
  """
  #comportamiento
  def arrancar(self,arrancamos = False):
    self.enmarcha = arrancamos
    if(self.enmarcha):
      chequeo = self.__cheque_interno()
      
    if(self.enmarcha and chequeo):
      return "El coche está en marcha"
    elif(self.enmarcha and chequeo == False ):
      return("Algo ha ido mal en el chequeo. no podemos arrancar")
    else:
      return "El coche está parado"
  
  def estado(self):
    return(f"El coche tiene {self.__ruedas} ruedas. Un ancho de {self.anchoChasis} y un largo de {self.largoChasis}")

  # Funcion encansulada metodo
  def __cheque_interno(self):
    print("Realizando chequeo interno 2")
    self.gasolina = "ok"
    self.aceite =  "ok"
    self.puertas = "cerradas"

    if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
      return True
    else:
      return False

      
#Instancia
miCoche = Coche()

print(f"El largo del coche es: {miCoche.largoChasis}")
print(miCoche.arrancar(True))
print(miCoche.estado())

print("\n-------------------------- A continuacion creamos el segundo objeto --------------------------\n")

miCoche2 = Coche()

print(f"El largo del coche es: {miCoche2.largoChasis}")
print(miCoche.arrancar())
print(miCoche2.estado())