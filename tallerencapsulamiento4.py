class Factura:
    def __init__(self, producto, precio):
        self.__producto = producto
        self.__precio = precio
        self.__iva = 0.19
    
    def set_producto(self, producto):
        self.__producto = producto
    
    def get_producto(self):
        return self.__producto
    
    def set_precio(self, precio):
        self.__precio = precio
    
    def get_precio(self):
        return self.__precio
    
    def calcular_total(self):
        total = self.get_precio() + (self.get_precio() * self.__iva)
        print(f"Producto: {self.get_producto()}")
        print(f"Precio: {self.get_precio()}")
        print(f"Total (con IVA): {total:.0f}")

factura = Factura("Portatil Acer", 3000000)
factura.calcular_total()
