class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        super().presentarse()
        print(f"Estudio la carrera de {self.carrera}.")


estudiante1 = Estudiante("Nico", 18, "Ingeniería de software")
estudiante1.presentarse()