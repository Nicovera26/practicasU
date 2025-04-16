class Estudiante:
    def __init__(self, nombre, notas):
        self.__nombre = nombre
        self.__notas = notas
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_nombre(self):
        return self.__nombre
    
    def set_notas(self, notas):
        self.__notas = notas
    
    def get_notas(self):
        return self.__notas
    
    def mostrar_datos(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Notas: {self.get_notas()}")

estudiante1 = Estudiante("Juan", [5.0, 2.9, 4.1])
estudiante2 = Estudiante("María", [3.2, 3.5, 3.0])
estudiante3 = Estudiante("Pedro", [3.5, 4.5, 3.2])

estudiante1.mostrar_datos()
estudiante2.mostrar_datos()
estudiante3.mostrar_datos()
