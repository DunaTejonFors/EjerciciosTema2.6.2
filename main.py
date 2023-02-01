class Alumno:
    Nombre = None
    Nota = None
    def __init__(self, nombre, nota):
        self.Nombre = nombre
        self.Nota = nota

    def mostrarAtributos(self):
        print("Nombre:", self.Nombre)
        print("Nota:", self.Nota)

    def estaAprobado(self):
        if self.Nota >= 5:
            print(self.Nombre,"tiene una nota de", self.Nota, ", ha aprobado.")
        else:
            print(self.Nombre, "tiene una nota de", self.Nota, ",no ha aprobado.")


Alumno1 = Alumno("María", 4.9)

Alumno1.mostrarAtributos()
Alumno1.estaAprobado()