from unittest import TestCase
from src.leilao.dominio import Usuario, Leilao, Lance


class TestLeilao(TestCase):

    def setUp(self):
        self.usr_ruan = Usuario("Ruan")
        self.usr_cinthia = Usuario("Cinthia")

        self.celular_leilao = Leilao("Celular Iphone 14")

        self.primeiro_lance = Lance(self.usr_ruan, 3000.0)
        self.segundo_lance = Lance(self.usr_cinthia, 3300.0)

    def test_deve_retornar_o_maior_e_menor_lance_quando_lancados_de_forma_crescente(self):
        self.celular_leilao.guardar_lance(self.primeiro_lance)
        self.celular_leilao.guardar_lance(self.segundo_lance)

        menor_valor_esperado = 3000.0
        maior_valor_esperado = 3300.0
        self.assertEqual(menor_valor_esperado, self.celular_leilao.menor_valor)
        self.assertEqual(maior_valor_esperado, self.celular_leilao.maior_valor)

    def test_deve_retornar_o_maior_e_menor_lance_quando_lancados_de_forma_decrescente(self):
        self.celular_leilao.guardar_lance(self.segundo_lance)
        self.celular_leilao.guardar_lance(self.primeiro_lance)

        menor_valor_esperado = 3000.0
        maior_valor_esperado = 3300.0
        self.assertEqual(menor_valor_esperado, self.celular_leilao.menor_valor)
        self.assertEqual(maior_valor_esperado, self.celular_leilao.maior_valor)

    def test_deve_retornar_o_menor_e_maior_valor_quando_possuir_um_lance(self):
        self.celular_leilao.guardar_lance(self.primeiro_lance)

        menor_valor_esperado = 3000.0
        maior_valor_esperado = 3000.0
        self.assertEqual(menor_valor_esperado, self.celular_leilao.menor_valor)
        self.assertEqual(maior_valor_esperado, self.celular_leilao.maior_valor)

    def test_deve_retornar_o_menor_e_maior_lance_quando_possuir_tres_lances(self):
        usr_nayara = Usuario("Nayara")
        terceiro_lance = Lance(usr_nayara, 3800.0)

        self.celular_leilao.guardar_lance(self.primeiro_lance)
        self.celular_leilao.guardar_lance(self.segundo_lance)
        self.celular_leilao.guardar_lance(terceiro_lance)

        menor_valor_esperado = 3000.0
        maior_valor_esperado = 3800.0
        self.assertEqual(menor_valor_esperado, self.celular_leilao.menor_valor)
        self.assertEqual(maior_valor_esperado, self.celular_leilao.maior_valor)

    def test_deve_adicionar_dois_lances_seguidos_da_mesma_pessoa(self):
        segundo_lance_local = Lance(self.usr_ruan, 1000)
        self.celular_leilao.guardar_lance(self.primeiro_lance)
        self.celular_leilao.guardar_lance(segundo_lance_local)

        quantidade_lances = len(self.celular_leilao.lances)
        self.assertEqual(2, quantidade_lances)

    def test_deve_permitir_adicionar_dois_lances_de_pessoas_diferentes(self):
        self.celular_leilao.guardar_lance(self.primeiro_lance)
        self.celular_leilao.guardar_lance(self.segundo_lance)

        quantidade_lances = len(self.celular_leilao.lances)
        self.assertEqual(2, quantidade_lances)

    def test_nao_deve_permitir_adicionais_dois_lances_seguidos_da_mesma_pessoa(self):
        segundo_lance_local = Lance(self.usr_ruan, 1000)
        self.celular_leilao.guardar_lance(self.primeiro_lance)
        self.celular_leilao.guardar_lance(segundo_lance_local)

        quantidade_lances = len(self.celular_leilao.lances)
        self.assertEqual(1, quantidade_lances)
