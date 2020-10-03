class Vehiculos():

  def __init__(self, marca, modelo):

    self.marca = marca
    self.modelo = modelo
    self.enmarcha = False
    self.acelera = False
    self.frena = False
  
  def arrancar(self):
    self.enmarcha = True
  
  def acelerar(self):
    self.acelera = True
  
  def frenar(self):
    self.frena = True

  def estado(self):
    return f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerador: {self.acelera} \nFreno: {self.frena}"

class Furgoneta(Vehiculos):
  def carga(self, cargar):
    self.caorgad = cargar
    if(self.caorgad):
      return "La furgoneta esta cargada"
    else:
      return "La furgoneta no esta cargada"

class Moto(Vehiculos):
  hpicar = ""
  def picar(self):
    self.hpicar = "Estoy picando la moto"
  
  def estado(self):
    return f"Marca: {self.marca} \nModelo: {self.modelo} \nEn Marcha: {self.enmarcha} \nAcelerador: {self.acelera} \nFreno: {self.frena} \n{self.hpicar}"

class CutraiMoto(Moto):
  pass

class VEletricos():
  def __init__(self, marca, modelo):
    super().__init__(marca, modelo)
    self.autonomia=100
  
  def cargarEnergia(self):
    self.cargando = True
  
class BisicletaEletrica(VEletricos,Vehiculos):
  pass


miMoto = Moto("Honda", "CBR")

print(miMoto.estado())
miMoto.picar()
print(miMoto.estado())
miForgoneta = Furgoneta("Renault", "Kangoo")
miForgoneta.arrancar()
print(miForgoneta.estado())
print(miForgoneta.carga(True))

miBici = BisicletaEletrica("Auteco","Prueba")
print(miBici.estado())