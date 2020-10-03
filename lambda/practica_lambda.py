def area_triangulo(base, altura):
  return (base*altura)/2

triangulo1= area_triangulo(5,7)/2
triangulo2= area_triangulo(9,6)/2

print(triangulo1)
print(triangulo2)

area_triangulo2 = lambda base, altura:(base*altura)/2
triangulo4= area_triangulo2(5,7)/2
triangulo5= area_triangulo2(9,6)/2

print(triangulo4)
print(triangulo5)

al_cubo = lambda numero:pow(numero, 3)
al_cubo2 = lambda numero:numero**3

print(al_cubo(12))
print(al_cubo2(12))

destacar_valor= lambda comision:"¡{}! $".format(comision)
destacar_valor2= lambda comision:f"¡{comision}! $"

comision_Car = 15585

print(destacar_valor(comision_Car))
print(destacar_valor2(comision_Car))
