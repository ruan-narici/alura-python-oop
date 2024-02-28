from Cpf import Cpf
from Cnpj import  Cnpj

class Documento:

    @staticmethod
    def cria_documento(documento):
        if len(str(documento)) == 11:
            return Cpf(documento)
        elif len(str(documento)) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")