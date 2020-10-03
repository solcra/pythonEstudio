import sqlite3

miConexion = sqlite3.connect("PrimeraBase")
miCursor=miConexion.cursor()
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón',15,'Deportes')")

# variosProductos = [
#   ("Camiseta",10,"Deportes"),
#   ("Jarron",90,"Cerámica"),
#   ("Camin",20,"Juguetería")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall()
print(variosProductos)

for producto in variosProductos:
  print(f"Nombre articulo: {producto[0]}")
  print(f"Precio: {producto[1]}")
  print(f"Categoria: {producto[2]}")

miConexion.commit()

miConexion.close()