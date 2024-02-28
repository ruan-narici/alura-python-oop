import re


email1 = "Meu numero e 3245-1242"
email2 = "Ola, tenho o telefone 2312-5312"
email3 = "Boa tarde, me chame no celular 2059-2312"
email4 = "Tenho o numero 23212-3123, 23214212 e 4312-3257"

emails = [email1, email2, email3]

padrao = "[0-9]{4}[-][0-9]{4}"
padrao_find_all = "[0-9]{4,5}[-]*[0-9]{4}"

for email in emails:
    numero_seguindo_padrao_encontrado = re.search(padrao, email)
    print(numero_seguindo_padrao_encontrado.group())

numeros_seguindo_padrao_encontrados = re.findall(padrao_find_all, email4)
print(numeros_seguindo_padrao_encontrados)