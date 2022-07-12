def isBisiesto(numero):
    if numero % 400 == 0:
        print("El año:",numero,"es bisiesto")
    elif numero % 4 == 0 and numero % 100 != 0:
        print("El año:",numero,"es bisiesto")
    else:
        print("El año no es bisiesto")

isBisiesto(2020)

