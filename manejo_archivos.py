from io import open

archivo_texto=open("archivo.txt","w")
frase="Estupendo dia para estudiar Python \n El dia miercoles"

archivo_texto.write(frase)
archivo_texto.close()

archivo_texto2=open("archivo.txt","r")
text = archivo_texto2.read()
text2 = archivo_texto2.readline()
archivo_texto2.close()
print(text)
print(text2)

archivo_texto3=open("archivo.txt","a")
archivo_texto3.write("\n"+frase)
archivo_texto3.close()

archivo_texto4 = open("archivo.txt","r")
print(archivo_texto4.read())
archivo_texto4.seek(0)
print("\nReinicio de puntero\n")
print(archivo_texto4.read())
archivo_texto4.seek(11)
print("\nReinicio de puntero\n")
print(archivo_texto4.read())
print("\nReinicio de puntero\n")
archivo_texto4.seek(0)
print(archivo_texto4.read(11))
archivo_texto4.seek(len(archivo_texto4.read())/2)

print(archivo_texto4.read())

print("\n")
archivo_texto5=open("archivo.txt","r+") # LECTURA Y ESCITURA
print(archivo_texto5.readline())
print(archivo_texto5.readlines())