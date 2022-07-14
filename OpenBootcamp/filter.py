from functools import reduce


numeros = [1,2,3,4,5,6,7,8,9,10]

impares = filter(lambda x: x % 2 == 1, numeros)
print(impares)

suma = reduce(lambda x,y: x+y, impares)
print(suma)