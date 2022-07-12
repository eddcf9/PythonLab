
from ast import Constant, Pow

import numpy


def areaTriangulo(base, altura):
    return (base * altura) / 2

def areaCirculo(radio):
    return numpy.pi * pow(radio, 2)


print(areaTriangulo(15, 45))
print(areaCirculo(50))