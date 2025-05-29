class ServicoConsultaUsuario:
    def __init__(self, repositorio: UsuarioRepositorio):
        self.repositorio = repositorio

    def buscar(self, tipo: str, valor: str):
        if tipo == "cpf":
            resultado = self.repositorio.buscar_por_cpf(valor)
            return [resultado] if resultado else []
        elif tipo == "nome":
            return self.repositorio.buscar_por_nome(valor)
        elif tipo == "id":
            try:
                id_int = int(valor)
            except ValueError:
                raise ValueError("ID deve ser numérico.")
            resultado = self.repositorio.buscar_por_id(id_int)
            return [resultado] if resultado else []
        elif tipo == "matricula":
            resultado = self.repositorio.buscar_por_matricula(valor)
            return [resultado] if resultado else []
        else:
            raise ValueError("Tipo de busca inválido.")
