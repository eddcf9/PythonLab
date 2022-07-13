class Alumno():
    Nombre = "Eduardo"
    Nota = 10

    def mostrarAtributos(self):
        return print("Hola",self.Nombre)

    def isAprobatoria(self):
        if self.Nota >= 6:
            print("Felicidades!, Has aprobado con", self.Nota)
        else:
            print("Lo siento, no has logrado aprobar")

A = Alumno()
A.mostrarAtributos()
A.isAprobatoria()
