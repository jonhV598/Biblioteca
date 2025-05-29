from dataclasses import dataclass
from enum import Enum
from typing import Optional
import re

class Categoria(Enum):
    ESTUDANTE = "estudante"
    PROFESSOR = "professor"
    VISITANTE = "visitante"

@dataclass
class Usuario:
    nome: str
    data_nascimento: str  # Idealmente datetime
    cpf: str
    telefone: str
    endereco: str
    categoria: Categoria
    email: Optional[str] = None
    matricula: Optional[str] = None
    departamento: Optional[str] = None

    def validar(self):
        if not self.nome or not self.data_nascimento or not self.cpf or not self.telefone or not self.endereco or not self.categoria:
            raise ValueError("Campos obrigatórios não preenchidos.")
        if not self.validar_cpf(self.cpf):
            raise ValueError("CPF inválido.")
        if self.email and not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            raise ValueError("Email inválido.")

    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        cpf = re.sub(r'[^0-9]', '', cpf)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        for i in [9, 10]:
            soma = sum(int(cpf[j]) * ((i+1) - j) for j in range(i))
            digito = ((soma * 10) % 11) % 10
            if digito != int(cpf[i]):
                return False
        return True
