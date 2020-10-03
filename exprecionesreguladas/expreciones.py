import re

cadena="Vamos a aprender expreciones regulares en Python. Python es un lenguaje de sintaxis sencilla"

print(re.search("aprender", cadena))

print(re.search("a prender", cadena))

textoBuscar="aprender"
textoEncontrado=''
if re.search(textoBuscar, cadena) is not None:
  textoEncontrado=re.search(textoBuscar, cadena)
  print("He econtrado el texto")
else:
  print("No he encontrado el texto")

print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())

textoBuscar="Python"
print(re.findall(textoBuscar, cadena))

lista_nombre=['Ana Gómez','María Martín','Sandra Lorez','Santiago Martín']

# Imprime al inicio
for elemento in lista_nombre:
  if re.findall('^Sandra', elemento):
    print(elemento)

# Imprime al contenedo del la ultima frase
for elemento in lista_nombre:
  if re.findall('Martín$',elemento):
    print(elemento)
lista_dominios=['http://pildorasinformaticas.es','ftp://pildorasinformaticas.es','http://pildorasinformaticas.com','ftp://pildorasinformaticas.com','http://informaticaemespaña.es']
#
for elemento in lista_dominios:
  if re.findall('es$', elemento):
    print(elemento)

for elemento in lista_dominios:
  if re.findall('^ftp', elemento):
    print(elemento)

#contiene elemento
for elemento in lista_dominios:
  if re.findall('[ñ]', elemento):
    print(elemento)

#Palabras
lista_humanos=['hombres','mujeres','mascotas','niñas','niños']

for elemento in lista_humanos:
  if re.findall('niñ[ao]s', elemento):
    print(elemento)


#Rangos
lista_nombres=['Ana','Pedro','María','Rosa','Sandra','Celia']

for elemento in lista_nombres:
  if re.findall('[o-t]', elemento):
    print(elemento)
  if re.findall('^[O-T]', elemento):
    print(elemento)
  if re.findall('[o-t]$', elemento):
    print(elemento)

lista_pedidos=['Ma1','Se1','Ma2','Ba1','Ma3','Va1','Va2','Ma4','MaA','Ma5','MaB','MaC']
for elemento in lista_pedidos:
  if re.findall('Ma[2-4]', elemento):
    print(elemento)

for elemento in lista_pedidos:
  if re.findall('Ma[2-4A-B]', elemento):
    print(elemento)

lista_pedidos2=['Ma.1','Se1','Ma2','Ba1','Ma:3','Va1','Va2','Ma4','MaA','Ma.5','MaB','Ma:C']
for elemento in lista_pedidos2:
  if re.findall('Ma[.:]', elemento):
    print(elemento)

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="sandra Lopez"
nombre5="Lara"
nombre6="Jara"

if re.match("Sandra", nombre1):
  print("Hemos encontrado el nombre")
else:
  print("No lo hemos encontrado")

if re.match("sandra", nombre4, re.IGNORECASE):
  print("Hemos encontrado el nombre")
else:
  print("No lo hemos encontrado")

if re.match(".ara", nombre6, re.IGNORECASE):
  print("Hemos encontrado el nombre")
else:
  print("No lo hemos encontrado")

cadena1="Lara López"
cadena2="1213123132"
cadena3="1dasdas1"

if re.match("\d", cadena1):
  print("Hemos encontrado el numero")
else:
  print("No lo hemos encontrado numero")

if re.search("López", nombre1):
  print("Hemos encontrado el apellido")
else:
  print("No hemos encontrado el apellido")

if re.search("López", nombre2):
  print("Hemos encontrado el apellido")
else:
  print("No hemos encontrado el apellido")


codigo1="fñkskhfajkfhkasdf71lkfjsdlfjsldf"
codigo2="kkasd71ljsldajladjas ldjsad asldjas"
codigo3="kllasjlkdjas dlasdalskdjlsadasñdjasdjlas"

if re.search("71", codigo1):
  print("Codigo encontrado")
else:
  print("Codigo no encontrado")


