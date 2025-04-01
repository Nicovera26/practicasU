from abc import ABC, abstractmethod

class Factura(ABC):
    @abstractmethod
    def calcular_total(self):
        pass

class FacturaSimple(Factura):
    def __init__(self, productos):
        self.productos = productos

    def calcular_total(self):
        return sum(producto['precio'] * producto['cantidad'] for producto in self.productos)


factura = FacturaSimple([{'precio': 5000, 'cantidad': 20}, {'precio': 20000, 'cantidad': 5}])
print(factura.calcular_total())