class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Vehiculo):
    def __init__(self, marca, modelo, nro_puertas):
        super().__init__(marca, modelo)
        self.nro_puertas = nro_puertas

class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor


c = Carro("Audi", "A4", "4 puertas")
m = Moto("KTM", "Duke 1390", "2 tiempos")


print(f"Carro: {c.marca}, {c.modelo}, {c.nro_puertas} puertas")
print(f"Moto: {m.marca}, {m.modelo}, motor {m.tipo_motor}")