class Pago:
    def __init__(self, monto, estado):
        self.__monto = monto
        self.__estado = estado
    
    def set_monto(self, monto):
        self.__monto = monto
    
    def get_monto(self):
        return self.__monto
    
    def set_estado(self, estado):
        self.__estado = estado
    
    def get_estado(self):
        return self.__estado
    
    def mostrar_estado(self):
        print(f"Monto: {self.get_monto()}")
        print(f"Estado: {self.get_estado()}")

pago = Pago(100000, "Pendiente")
pago.mostrar_estado()
