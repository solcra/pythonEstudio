def areaTringulo(base,altura):
  """
  Calcula al area de un triangulo dado
  >>> areaTringulo (3,6)
  9.0
  """
  return (base*altura)/2

def areaTringulo2(base,altura):
  """
  Calcula al area de un triangulo dado
  >>> areaTringulo2 (3,6)
  'El area del triangulo es: 9.0'
  """
  return "El area del triangulo es: " +str((base*altura)/2)

import doctest
doctest.testmod()