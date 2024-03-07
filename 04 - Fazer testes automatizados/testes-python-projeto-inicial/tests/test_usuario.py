from src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def usuario():
    return Usuario("Ruan", 300)

@pytest.fixture
def leilao():
    return Leilao("Celular")

def test_deve_subtrair_valor_da_carteira_do_usuario_apos_propor_um_lance(usuario, leilao):
    usuario.propor_lance(leilao, 300)
    assert usuario.carteira == 0

def test_deve_permitir_propor_valor_abaixo_da_carteira(usuario, leilao):
    usuario.propor_lance(leilao, 50)
    assert usuario.carteira == 250

def test_deve_permitir_propro_valor_igual_a_carteira(usuario, leilao):
    usuario.propor_lance(leilao, 300)
    assert usuario.carteira == 0

def test_nao_deve_permitir_propro_valor_maior_que_a_carteira(usuario, leilao):
    with pytest.raises(ValueError):
        usuario.propor_lance(leilao, 400)
