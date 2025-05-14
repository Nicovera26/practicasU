class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Empleado:
    def trabajar(self):
        print("Estoy trabajando.")

class Deportista:
    def entrenar(self):
        print("Estoy entrenando.")

class EmpleadoDeportista(Persona, Empleado, Deportista):
    pass


EmpleadoDeportista1 = EmpleadoDeportista("Carlos")
print(f"Nombre: {EmpleadoDeportista1.nombre}")
EmpleadoDeportista1.trabajar()
EmpleadoDeportista1.entrenar()


print(EmpleadoDeportista.mro())