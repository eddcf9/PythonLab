class Alumno():
    Nombre = "Eduardo"
    Nota = 10

    def mostrarAtributos(self):
        return print("Hola",self.Nombre + ", tu calificacion es:",self.Nota)

A = Alumno()
A.mostrarAtributos()
