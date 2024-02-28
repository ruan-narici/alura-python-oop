class Data:
    def __init__(self, dia :int, mes :int, ano :int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatar(self):
        print("{0:02d}/{1:02d}/{2:04d}".format(
            self.__dia,
            self.__mes,
            self.__ano
        ))
