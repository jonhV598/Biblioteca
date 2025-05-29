import pytest
from servico_cadastro_usuario import ServicoCadastroUsuario
from servico_consulta_usuario import ServicoConsultaUsuario
from usuario import Usuario, Categoria
from servico_cadastro_usuario import UsuarioRepositorio

@pytest.fixture
def repositorio_populado():
    repo = UsuarioRepositorio()
    servico = ServicoCadastroUsuario(repo)
    usuarios = [
        {"nome": "kakarotto", "data_nascimento": "1990-01-01", "cpf": "12345678909", "telefone": "1111", "endereco": "Rua A", "categoria": Categoria.ESTUDANTE, "matricula": "123"},
        {"nome": "vegeta", "data_nascimento": "1995-02-02", "cpf": "98765432100", "telefone": "2222", "endereco": "Rua B", "categoria": Categoria.PROFESSOR, "matricula": "456"},
    ]
    for u in usuarios:
        servico.cadastrar(u)
    return repo

def test_busca_por_nome(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    resultados = servico.buscar("nome", "ka")
    assert len(resultados) == 2

def test_busca_por_cpf(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    resultados = servico.buscar("cpf", "12345678909")
    assert len(resultados) == 1
    assert resultados[0].nome == "kakarotto"

def test_busca_inexistente(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    resultados = servico.buscar("cpf", "00000000000")
    assert resultados == []

def test_busca_por_id_valido(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    resultados = servico.buscar("id", "0")
    assert len(resultados) == 1

def test_busca_por_id_invalido(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    resultados = servico.buscar("id", "10")
    assert resultados == []

def test_tipo_de_busca_invalido(repositorio_populado):
    servico = ServicoConsultaUsuario(repositorio_populado)
    with pytest.raises(ValueError, match="Tipo de busca inválido."):
        servico.buscar("genero", "teste")
