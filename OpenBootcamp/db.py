from getpass import getpass
import sqlite3

def main2():
    crearUsuario(2, "edd", "pass2")


def main():
    username = input("Nombre de usuario: ")
    password = getpass("Contraseña: ")

    if verificaCredenciales(username, password):
        print("Login correcto")
    else:
        print("Datos incorrectos")



def verificaCredenciales(username, password):
    conn = sqlite3.connect("midb.db", isolation_level=None)
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    row = cursor.execute(query)
    data = row.fetchone()

    cursor.close()
    conn.close()

def crearUsuario(identificador, usuario, clave):
    conn = sqlite3.connect("midb.db", isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)'''
    row = cursor.execute(query, (identificador, usuario, clave))

    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()
    #main2()

