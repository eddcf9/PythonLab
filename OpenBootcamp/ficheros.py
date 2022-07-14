#Creacion del fichero y escritura
f = open('datos.txt', "w")
f.write("Hola desde el fichero\n")
f.close()

#Apertura y lectura del archivo
f = open('datos.txt', "r")
contenido = f.read()

print(contenido)
f.close()

