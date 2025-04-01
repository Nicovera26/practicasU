from abc import ABC, abstractmethod

class Usuario(ABC):
    @abstractmethod
    def autenticar(self, contraseña):
        pass

class UsuarioSimple(Usuario):
    def __init__(self, contraseña):
        self.contraseña = contraseña

    def autenticar(self, contraseña):
        return self.contraseña == contraseña

usuario = UsuarioSimple('987654321')
print(usuario.autenticar('Nic0las'))