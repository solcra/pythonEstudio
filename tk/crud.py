from tkinter import *
from tkinter import messagebox
import sqlite3

# FUnciones
def conexionBBDD():
  miConexion = sqlite3.connect("Usuaiorios")
  miCursor=miConexion.cursor()
  try:
    miCursor.execute('''
      CREATE TABLE DATOSUSUARIOS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_USUARIO VARCHAR(50),
        PASSWPRD VARCHAR(50),
        APELLIDO VARCHAR(50),
        DIRECCION VARCHAR(100),
        COMENTARIOS VARCHAR(200)
      )
    ''')

    messagebox.showinfo("BBDD", "BBDD creada con éxito")
  except:
    messagebox.showwarning("¡Atención", "La BBDD ya existe")

#Salir de la palicacion
def salirAplicacion():
  valor=messagebox.askquestion("Salir","¿Deseas salir de la palicación?")
  if valor == "yes":
    root.destroy()

#Limpiar los cambios
def limpiasCampos():
  miNombre.set("")
  miID.set("")
  miApellido.set("")
  miPass.set("")
  miDirecion.set("")
  textoComentario.delete(1.0, END)

#Crear
def crear():
  miConecion=sqlite3.connect("Usuaiorios")
  miCursor=miConecion.cursor()
  """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,'"+miNombre.get()+
    "','"+miPass.get()+
    "','"+miApellido.get()+
    "','"+miDirecion.get()+
    "','"+textoComentario.get("1.0", END)+"')")"""
  datos=miNombre.get(),miPass.get(),miApellido.get(),miDirecion.get(),textoComentario.get("1.0", END)
  miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))
  miConecion.commit()
  messagebox.showinfo("BBDD", "Registro insertado con exito")

#Leer
def leer():
  miConexion=sqlite3.connect("Usuaiorios")
  miCursor=miConexion.cursor()
  miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+ miID.get())
  elUsuario = miCursor.fetchall()

  for usuario in elUsuario:
    miID.set(usuario[0])
    miNombre.set(usuario[1])
    miPass.set(usuario[2])
    miApellido.set(usuario[3])
    miDirecion.set(usuario[4])
    textoComentario.insert(1.0, usuario[5])
  miConexion.commit()

#actualizar
def actaulizar():
  miConecion=sqlite3.connect("Usuaiorios")
  miCursor=miConecion.cursor()
  #miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='"+miNombre.get()+"', PASSWPRD='"+miPass.get()+"', APELLIDO='"+miApellido.get()+"', DIRECCION= '"+miDirecion.get()+"', COMENTARIOS='"+textoComentario.get("1.0", END)+"' WHERE ID="+miID.get())
  datos=miNombre.get(),miPass.get(),miApellido.get(),miDirecion.get(),textoComentario.get("1.0", END)
  miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO=? , PASSWPRD=? , APELLIDO=? , DIRECCION=? , COMENTARIOS=? WHERE ID="+miID.get(),datos)
  miConecion.commit()
  messagebox.showinfo("BBDD", "Registro actualizado con exito")

# Eliminar
def eliminar():
  miConecion=sqlite3.connect("Usuaiorios")
  miCursor=miConecion.cursor()
  miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ miID.get())
  miConecion.commit()
  messagebox.showinfo("BBDD", "Borrado con exito")

# End Funciones

root=Tk()

# Menu
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar campos", command=limpiasCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actaulizar", command=actaulizar)
crudMenu.add_command(label="Borrar", command=eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)
# End Menu

# Body
miFrame=Frame(root)
miFrame.pack()

miID = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPass = StringVar()
miDirecion = StringVar()

cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPas=Entry(miFrame, textvariable=miPass)
cuadroPas.grid(row=2, column=1, padx=10, pady=10)
cuadroPas.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDirecion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

# ETIQUETAS LABEL

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direcionLabel = Label(miFrame, text="Direccion:")
direcionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)
# End Body

# footer
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Create", command=crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Read", command=leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActaulizar=Button(miFrame2, text="Update", command=actaulizar)
botonActaulizar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Delet", command=eliminar)
botonBorrar.grid(row=1, column=4, sticky="e", padx=10, pady=10)
# End Foter

root.mainloop()