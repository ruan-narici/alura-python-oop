from Documento import Documento
from Telefone import Telefone
from DataHoraBr import DataHoraBr
from Cep import Cep

# CPF e CNPJ
exemplo_cpf = "62636673628"
exemplo_cnpj = "60705716000116"

documento_cpf = Documento.cria_documento(exemplo_cpf)
documento_cnpj = Documento.cria_documento(exemplo_cnpj)

print(documento_cpf)
print(documento_cnpj)

# TELEFONE
numero_telefone = "5577991586189"
telefone = Telefone(numero_telefone)
print(telefone)

# DATA E HORA
dataHora = DataHoraBr()
print(dataHora.momento_registro())
print(dataHora)
print(dataHora.tempo_cadastrado())

# CEP
numero_cep = "45028185"
cep = Cep(numero_cep)
print(cep)
bairro, cidade, estado = cep.acessa_api_via_cep()
print(bairro, cidade, estado)