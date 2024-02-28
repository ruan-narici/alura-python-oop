from Programa import Programa


class Filme(Programa):

    def __init__(self, nome: str, ano: int, duracao: int):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self.likes}'
