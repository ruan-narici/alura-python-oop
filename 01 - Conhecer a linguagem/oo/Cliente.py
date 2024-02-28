class Cliente:

    def __init__(self, nome :str):
        self.__nome = nome.lower().capitalize()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        self.__nome = nome
