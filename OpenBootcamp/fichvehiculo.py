import pickle 

#Creamos la clase
class Vehiculo():
    nombre = ''
    velocidad = ''
    modelo = ''

    def __init__(self, nombre, velocidad, modelo):
        self.nombre = nombre
        self.velocidad = velocidad
        self.modelo = modelo

    def obtenerAtributos(self):
        return self.nombre, self.modelo, self.velocidad


#Guardamos la instancia 
V = Vehiculo('Chevy', '180', '145588')
f = open('instancia.bin', 'wb')
pickle.dump(V, f)
f.close()

#Recuperamos la instancia
f = open('instancia.bin', 'rb')
auto = pickle.load(f)
f.close()

print(type(auto))
print(auto.obtenerAtributos())