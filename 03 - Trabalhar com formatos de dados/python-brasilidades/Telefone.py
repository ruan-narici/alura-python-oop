import re


class Telefone:

    def __init__(self, telefone):
        if self.valida(telefone):
            self.telefone = telefone
        else:
            raise ValueError("Telefone inválido!")

    def __str__(self):
        return self.formatar()

    def valida(self, telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        if re.findall(padrao, str(telefone)):
            return True
        else:
            return False

    def formatar(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.telefone)
        numero_formatado = (f'+{resposta.group(1)} ({resposta.group(2)}) '
                            f'{resposta.group(3)}-{resposta.group(4)}')
        return numero_formatado