from tkinter import *

raiz = Tk()
raiz.title("Ventana de pruebas")
raiz.resizable(1,1)
#raiz.iconbitmap("nombre.ico")
#raiz.geometry("650x350") tamaño de la raiz
raiz.config(bg="#000")
miFrame=Frame()
miFrame.pack()
#miFrame.pack(side="right", anchor="n") Posicionamiento
#miFrame.pack(fill="x") espande al ancho
#miFrame.pack(fill="y", expand="True")  espande al alto
#miFrame.pack(fill="both", expand="True")
miFrame.config(bg="#f1f1f1")
miFrame.config(width="650", height="350" )
miFrame.config(bd=35)
miFrame.config(relief="groove")
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")
miFrame.config(cursor="pirate")
raiz.mainloop()
