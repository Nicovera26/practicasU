from abc import ABC, abstractmethod

class Estudiante(ABC):
    @abstractmethod
    def calcular_promedio(self):
        pass

class EstudianteRegular(Estudiante):
    def __init__(self, notas):
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)


estudiante = EstudianteRegular([3.5, 4.0, 3.8, 4.2, 3.9])
print(estudiante.calcular_promedio())