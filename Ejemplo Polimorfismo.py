class Coche():
  def desplazamiento(self):
    print("Me despazo utilizando cuatro ruedoas")

class Motos():
  def desplazamiento(self):
    print("Me despazo utilizando dos ruedas")

class Camion():
  def desplazamiento(self):
    print("Me desplazo utilizando seis ruedas")

miVeiculo = Motos()

miVeiculo.desplazamiento()

miVeiculo2 = Coche()

miVeiculo2.desplazamiento()

miVeiculo3 = Camion()

miVeiculo3.desplazamiento()

print("\n********************\n")

def despazamientoVehiculo(vehiculo):
  vehiculo.desplazamiento()

miVeiculop=Camion()
despazamientoVehiculo(miVeiculop)

miVeiculop2=Coche()
despazamientoVehiculo(miVeiculop2)

miVeiculop3=Motos()
despazamientoVehiculo(miVeiculop3)