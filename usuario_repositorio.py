class UsuarioRepositorio:
    def __init__(self):
        self._usuarios = []

    def adicionar(self, usuario: Usuario):
        if self.buscar_por_cpf(usuario.cpf):
            raise ValueError("CPF já cadastrado.")
        self._usuarios.append(usuario)

    def buscar_por_cpf(self, cpf: str) -> Usuario:
        return next((u for u in self._usuarios if u.cpf == cpf), None)

    def buscar_por_nome(self, nome: str) -> list:
        return [u for u in self._usuarios if nome.lower() in u.nome.lower()]

    def buscar_por_id(self, id_: int) -> Usuario:
        # ordenada pela ordem de inserção
        try:
            return self._usuarios[id_]
        except IndexError:
            return None

    def buscar_por_matricula(self, matricula: str) -> Usuario:
        return next((u for u in self._usuarios if u.matricula == matricula), None)
