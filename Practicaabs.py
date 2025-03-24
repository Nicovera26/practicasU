from abc import ABC, abstractmethod

class formapago(ABC):
    
    @abstractmethod
    def procesar_pago(self, monto):
        pass
    
class efectivo(formapago):
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)

class tarjeta_credito(formapago):
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)
    
class tarjeta_debito(formapago):
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)
    
class tarjeta_nequi(formapago):
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)
    
class daviplata(formapago):
    def procesar_pago(self, monto):
        return super().procesar_pago(monto)
    
def realizar_pago(formapago, monto):
        print(f"Pago realizado con {formapago.procesar_pago(monto)}")

pago_efectivo = efectivo()
pago_tarjeta_credito = tarjeta_credito()
pago_tarjeta_nequi = tarjeta_nequi()
pago_tarjeta_debito = tarjeta_debito()
pago_daviplata = daviplata()

realizar_pago(pago_efectivo, 100)
realizar_pago(pago_tarjeta_credito, 100)
realizar_pago(pago_tarjeta_nequi, 100)
realizar_pago(pago_tarjeta_debito, 100) 
realizar_pago(pago_daviplata, 100)