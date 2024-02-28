from validate_docbr import CNPJ


class Cnpj:

    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        return CNPJ().validate(documento)

    def formata(self):
        return CNPJ().mask(str(self.cnpj))
