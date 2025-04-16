class Cuenta:
    def __init__(self, usuario, contrasena):
        self.__usuario = usuario
        self.__contrasena = contrasena
    
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def get_usuario(self):
        return self.__usuario
    
    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena
    
    def get_contrasena(self):
        return self.__contrasena
    
    def validar_acceso(self, usuario, contrasena):
        if usuario == self.get_usuario() and contrasena == self.get_contrasena():
            print("Acceso válido")
        else:
            print("Acceso denegado")

cuenta = Cuenta("Nico26", "123456")
cuenta.validar_acceso("Nico26", "123456")
cuenta.validar_acceso("Nico26", "123456")
