class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoPerecedero(Producto):
    def __init__(self, nombre, precio, fecha_vencimiento):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento


producto1 = ProductoPerecedero("Leche", 3500, "2025-04-10")
print(f"Producto: {producto1.nombre}, Precio: {producto1.precio}, Vencimiento: {producto1.fecha_vencimiento}")