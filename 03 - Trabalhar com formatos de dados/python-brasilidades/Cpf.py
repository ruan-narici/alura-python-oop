from validate_docbr import CPF


class Cpf:

    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formata()

    def valida(self, documento):
        return CPF().validate(documento)

    def formata(self):
        return CPF().mask(str(self.cpf))
