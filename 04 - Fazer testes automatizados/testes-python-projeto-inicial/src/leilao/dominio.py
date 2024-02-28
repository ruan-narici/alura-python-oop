import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

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
        if not self.__lances or self.__lances[-1].usuario != lance.usuario:
            if lance.valor > self.maior_valor:
                self.maior_valor = lance.valor
            if lance.valor < self.menor_valor:
                self.menor_valor = lance.valor
            self.__lances.append(lance)
