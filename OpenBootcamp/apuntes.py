#import logging
#from functools import reduce

#logging.basicConfig(level=logging.WARNING)
#logging.warning("Hace Calor")
#filter() aplica una funcion a todos los elementos de una lista

'''numeros = [1,2,3,4,5,6,7,8,9,10]

def miFuncion(x):
    if x % 2 == 0:
        return True

    return False

resultado = filter(miFuncion, numeros) #con funcion 
resultado2 = filter(lambda x: x%2==1, numeros) #con funcion anonima
print(list(resultado))
print(resultado2)


#funcion map
resultado3 = map(lambda x: x*x, [2,4,6,8])
print(resultado3)

res = reduce(lambda a,b: a+b, [1,2,3,4,5])
print(res) '''