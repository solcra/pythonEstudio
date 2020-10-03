from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
def infoAdicional():
  messagebox.showinfo("Pocesador de Carlos", "Procesador de texto version 2020")

def infoLicencia():
  messagebox.showwarning("Licencia", "Prodcto bajo licencia OPG")

def salirAplicacion():
  valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
  print(valor)
  if valor == "yes":
    root.destroy()
def cerrarAplicacion():
  valor = messagebox.askokcancel("Salir","¿Deseas salir de la aplicacion?")
  print(valor)
  if valor == True:
    root.destroy()
  valor2 = messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
  if valor2 == False:
    root.destroy()

def abreFichero():
  fichero = filedialog.askopenfilename(title="Abrir", initialdir="./", filetypes=(("Ficheros de Excl","*.xlsx"),("Ficheros de texto","*.txt")))
  print(fichero)

barraMenu=Menu(root)
root.config(menu=barraMenu)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarAplicacion)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=infoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

varOpcion=IntVar()
playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def imprimir():
  print(varOpcion.get())
  if varOpcion.get()==1:
    etiqueta.config(text="Has elegido masculino")
  else:
    etiqueta.config(text="Has elegido famenino")

def opcionesViaje():
  opcionEscogida=""
  if(playa.get()==1):
    opcionEscogida+=" Playa"
  if(montagna.get()==1):
    opcionEscogida+=" montaña"
  if(turismoRural.get()==1):
    opcionEscogida+=" Turismo Rural"
  
  textoFinal.config(text=opcionEscogida)

  

Label(root, text="Genero:").pack()

Radiobutton(root, text="Maculino", variable=varOpcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rutal", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()
etiqueta = Label(root)
etiqueta.pack()

textoFinal = Label(root)
textoFinal.pack()

root.mainloop()