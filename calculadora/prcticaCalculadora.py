from tkinter import *

raiz=Tk()

miFrame=Frame()

miFrame.pack()

operacion=""
resultado = 0
resta = False

# --------- Pantalla --------- 

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black",fg="#03f943", justify="right")

# --------- Pulsaciones teclado ---------

def numeroPulsado(numero):
  global operacion
  if operacion !="":
    numeroPantalla.set(numero)
    operacion = ""
  else:
    numeroPantalla.set(numeroPantalla.get() + numero)


# --------- Operaciones ---------
def operaciones(num,infOperacion):
  global operacion
  global resultado
  global resta
  print(resultado)
  print(int(num))
  if infOperacion == "suma":
    resultado +=int(num)
  
  if infOperacion == "resta":
    if resta == False:
      resultado = int(num)
      resta = True
    else:
      resultado -= int(num)
  
  if infOperacion == "multiplicacion":
    resultado/=int(num)
  
  if infOperacion == "divicion":
    resultado*=int(num)
  
  operacion = infOperacion
  numeroPantalla.set(resultado)


# --------- Operacion igaul ---------
def igaul():
  global resultado
  numeroPantalla.set(resultado+int(numeroPantalla.get()))
  resultado=0

# --------- Fila uno --------- 
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDivi=Button(miFrame, text="/", width=3, command=lambda:operaciones(numeroPantalla.get(),"divicion"))
botonDivi.grid(row=2, column=4)

# --------- Fila dos --------- 
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:operaciones(numeroPantalla.get(),"multiplicacion"))
botonMult.grid(row=3, column=4)

# --------- Fila tres --------- 
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes=Button(miFrame, text="-", width=3, command=lambda:operaciones(numeroPantalla.get(),"resta"))
botonRes.grid(row=4, column=4)

# --------- Fila cuatro --------- 
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=5, column=1)
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:igaul())
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:operaciones(numeroPantalla.get(),"suma"))
botonSuma.grid(row=5, column=4)

raiz.mainloop()