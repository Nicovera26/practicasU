class Animal:
    def hacer_sonido(self):
        print("Sonido genérico")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

animal = Animal()
animal.hacer_sonido()

perro = Perro()
perro.hacer_sonido()

gato = Gato()
gato.hacer_sonido()