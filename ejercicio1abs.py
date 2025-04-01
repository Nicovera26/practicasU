from abc import ABC, abstractmethod

class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual


empleado = EmpleadoTiempoCompleto(3000)
print(empleado.calcular_salario())