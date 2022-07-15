import sqlite3

conexion = sqlite3.connect("midb.db")

def crearUser():
    id = int(input("Ingresa el id: "))
    nombre = input("Ingresa el nombre: ")
    apellido = input("Ingresa el apellido: ")
    conexion.execute("INSERT INTO alumnos(id, nombre, apellido) VALUES(?,?,?)", (id, nombre, apellido))

    conexion.commit()
    conexion.close()



def buscarUser():
    nombre = input("Ingrese el nombre del alumno: ")
    cursor = conexion.execute("SELECT * FROM alumnos WHERE nombre=?", (nombre, ))
    fila = cursor.fetchone()
    if fila != None:
        print(fila)
    else:
        print("No existe el alumno")

    conexion.close()


if __name__ == '__main__':
    #crearUser()
    buscarUser()