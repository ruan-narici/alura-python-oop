class Programa:

    def __init__(self, nome: str, ano: int):
        self._nome = nome.lower().title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome.lower().title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.likes}'
