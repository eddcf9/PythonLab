def isPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            print("El numero:",numero, "no es primo")
            return False
    print("Es primo")
    return True

isPrimo(8)