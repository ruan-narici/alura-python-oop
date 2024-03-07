import sys
import pytest



class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def __valor_eh_valido(self, valor):
        return self.__carteira >= valor

    def propor_lance(self, leilao, valor):
        if self.__valor_eh_valido(valor):
            lance = Lance(self, valor)
            leilao.guardar_lance(lance)
            self.__carteira -= valor
        else:
            raise ValueError("Saldo insuficiente")

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.menor_valor = sys.float_info.max
        self.maior_valor = sys.float_info.min

    @property
    def lances(self):
        return self.__lances[:]

    def guardar_lance(self, lance):
        if self.__nao_tem_lances() or self.__lance_de_usuario_diferente(lance) and self.__lance_valido(lance):
            if lance.valor > self.maior_valor:
                self.maior_valor = lance.valor
            if lance.valor < self.menor_valor:
                self.menor_valor = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError("Erro ao guardar lance")

    def __nao_tem_lances(self):
        return not self.__lances

    def __lance_de_usuario_diferente(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def __lance_valido(self, lance):
        return lance.valor > self.__lances[-1].valor
