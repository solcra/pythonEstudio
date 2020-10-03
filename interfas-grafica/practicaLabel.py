from tkinter import *

root = Tk()
miFrame=Frame(root,width=500, height=400)
miFrame.pack()

minombre =StringVar()

miLabel=Label(miFrame, text="Hola Carlos", fg="#a1a1a1", font=("Comic Sans MS",18))
#miLabel.pack()
miLabel.grid(row=1, column=0)


miImagen=PhotoImage(file="interfas-grafica/favicon-72.png")
miLabelImagen = Label(miFrame, image=miImagen)
miLabelImagen.grid(row=0, column=0)
miTextNombre = Entry(miFrame, textvariable=minombre)
miTextNombre.grid(row=2,column=1, pady=3 , padx=2)
miLabelNombre = Label(miFrame, text="Cual es tu nombre: ")
miLabelNombre.grid(row=2,column=0, sticky="e", pady=3 , padx=2)

miTextApellido = Entry(miFrame)
miTextApellido.grid(row=3,column=1, pady=3 , padx=2)
miLabelApellido = Label(miFrame, text="Cual es tu apellido: ")
miLabelApellido.grid(row=3,column=0, sticky="e", pady=3 , padx=2)

miTextDireccion = Entry(miFrame)
miTextDireccion.grid(row=4,column=1, pady=3 , padx=2)
miLabelDireccion = Label(miFrame, text="Cual es tu direccion: ")
miLabelDireccion.grid(row=4,column=0, sticky="e", pady=3, padx=2)


miTextPass = Entry(miFrame)
miTextPass.grid(row=5,column=1, pady=3 , padx=2)
miTextPass.config(show="*")
miLabelPass = Label(miFrame, text="Contraseña: ")
miLabelPass.grid(row=5,column=0, sticky="e", pady=3, padx=2)



miTextAreaComentarios = Text(miFrame, width=16, height=5)
miTextAreaComentarios.grid(row=6,column=1, pady=3 , padx=2)
miLabelTextArea = Label(miFrame, text="Comentario: ")
miLabelTextArea.grid(row=6,column=0, sticky="e", pady=3, padx=2)

scrollVerti=Scrollbar(miFrame, command=miTextAreaComentarios.yview)
scrollVerti.grid(row=6,column=2, sticky="nsew")
miTextAreaComentarios.config(yscrollcommand=scrollVerti.set)
def codigoBoton():
  minombre.set("Carlos")

botonEnvio=Button(root, text="Envio", command=codigoBoton)
botonEnvio.pack()



root.mainloop()