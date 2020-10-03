import sqlite3

miConexion=sqlite3.connect("GestionPorductos3")
miCursor=miConexion.cursor()

"""miCursor.execute('''
  CREATE TABLE PRODUCTOS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20)
  )
''')

productos=[
  ("pelotas",20, "juguetería"),
  ("pantalón",15, "confección"),
  ("destornillador",25, "ferretería"),
  ("jarrón",45, "cerámica")
]"""

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES (NULL,'pantalón',20,'jugueteria')")

# Actualizacion
"""miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35  WHERE NOMBRE_ARTICULO = 'pelotas'")

"""
#miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

miCursor.execute("SELECT * FROM PRODUCTOS")

productos = miCursor.fetchall()

print(productos)



miConexion.commit()
miConexion.close()