class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        print(
            "A conta de {0} com numero {1} foi criada com sucesso!"
              .format(self.__titular, self.__numero)
        )

    def extrato(self) -> None:
        print("R$ {0}".format(self.__saldo))

    def depositar(self, valor :float) -> bool:
        if (valor <= 0):
            return False

        self.__saldo += valor
        return True

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_disponivel > valor_a_sacar

    def sacar(self, valor :float) -> bool:
        if (not self.__pode_sacar(valor)):
            return False

        self.__saldo -= valor
        return True

    def transferir(self, valor :float ,destino) -> bool:
        if (not self.sacar(valor)):
            return False

        if (not destino.depositar(valor)):
            return False

        return True

    def get_numero(self) -> int:
        return self.__numero

    def get_titular(self) -> str:
        return self.__titular

    def get_saldo(self) -> float:
        return self.__saldo

    def get_limite(self) -> float:
        return self.__limite

    def set_limite(self, valor :int) -> bool:
        if (valor < 0):
            return False

        self.__limite = valor
        return True