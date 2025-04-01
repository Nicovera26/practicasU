from abc import ABC, abstractmethod

class Menu(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class MenuSencillo(Menu):
    def __init__(self, opciones):
        self.opciones = opciones

    def ejecutar(self):
        for opcion in self.opciones:
            print(f"Ejecutando: {opcion}")


menu = MenuSencillo(['Opción 1', 'Opción 2', 'Opción 3'])
menu.ejecutar()