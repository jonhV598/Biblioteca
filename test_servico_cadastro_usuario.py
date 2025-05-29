import pytest
from servico_cadastro_usuario import ServicoCadastroUsuario, UsuarioRepositorio
from usuario import Categoria

def test_cadastro_usuario_sucesso():
    repositorio = UsuarioRepositorio()
    servico = ServicoCadastroUsuario(repositorio)

    dados = {
        "nome": "kakarotto",
        "data_nascimento": "1995-05-21",
        "cpf": "12345678909",  # CPF válido fictício
        "telefone": "11999999999",
        "endereco": "Rua A, 123",
        "categoria": Categoria.ESTUDANTE,
        "email": "goku@email.com"
    }

    usuario = servico.cadastrar(dados)
    assert usuario in repositorio._usuarios

def test_cadastro_com_cpf_repetido():
    repositorio = UsuarioRepositorio()
    servico = ServicoCadastroUsuario(repositorio)

    dados = {
        "nome": "vegeta",
        "data_nascimento": "1980-02-02",
        "cpf": "12345678909",
        "telefone": "11988888888",
        "endereco": "Rua B, 456",
        "categoria": Categoria.PROFESSOR
    }

    servico.cadastrar(dados)
    with pytest.raises(ValueError, match="CPF já cadastrado."):
        servico.cadastrar(dados)

def test_email_invalido():
    repositorio = UsuarioRepositorio()
    servico = ServicoCadastroUsuario(repositorio)

    dados = {
        "nome": "bulma",
        "data_nascimento": "1990-01-01",
        "cpf": "98765432100",
        "telefone": "11977777777",
        "endereco": "Rua C, 789",
        "categoria": Categoria.VISITANTE,
        "email": "emailinvalido"
    }

    with pytest.raises(ValueError, match="Email inválido."):
        servico.cadastrar(dados)
