from usuario import Usuario
from typing import List

class UsuarioRepositorio:
    def __init__(self):
        self._usuarios = []

    def adicionar(self, usuario: Usuario):
        if self.buscar_por_cpf(usuario.cpf):
            raise ValueError("CPF já cadastrado.")
        self._usuarios.append(usuario)

    def buscar_por_cpf(self, cpf: str) -> Usuario:
        return next((u for u in self._usuarios if u.cpf == cpf), None)

class ServicoCadastroUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def cadastrar(self, dados: dict):
        usuario = Usuario(**dados)
        usuario.validar()
        self.repositorio.adicionar(usuario)
        return usuario
