#Funcion
def generaPares(limite):
  num=1
  miLista=[]
  while num<limite:
    miLista.append(num*2)
    num +=1
  return miLista
print(generaPares(10))

#Interador
def generaPares2(limite):
  num=1
  while num<limite:
    yield num*2
    num +=1
devuelvePares=generaPares2(10)
for i in devuelvePares:
  print(i)
devuelvePares2=generaPares2(10)
print(next(devuelvePares2))
print("Mas lineas comando")
print(next(devuelvePares2))
print("Mas lineas comando")
print(next(devuelvePares2))
print("Mas lineas comando")

def devuelve_ciudaddes(*ciudades):
  for elementi in ciudades:
    for subElenti in elementi:
      yield subElenti

ciudades_debueldas=devuelve_ciudaddes("Madril", "Barcelona","Bilbao","Valencia")
print(next(ciudades_debueldas))
print(next(ciudades_debueldas))

def devuelve_ciudaddes2(*ciudades):
  for elementi in ciudades:
    yield from elementi

ciudades_debueldas2=devuelve_ciudaddes2("Madril", "Barcelona","Bilbao","Valencia")
print(next(ciudades_debueldas2))
print(next(ciudades_debueldas2))
