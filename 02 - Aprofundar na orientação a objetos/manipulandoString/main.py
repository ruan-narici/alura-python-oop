from ExtratorURL import ExtratorURL


url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"

# params = url.split("?")[1]
# arrayTuples = list()
#
# params = params.split("&");
#
# for param in params:
#     key = param.split("=")[0]
#     value = param.split("=")[1]
#     arrayTuples.append((key, value))
#
# print(arrayTuples)

argumento = ExtratorURL(url)
moeda_origem, moeda_destino, moeda_valor = argumento.extrair_valores()

# print(f'Moeda origem: {moeda_origem}, Moeda destino: {moeda_destino}, Valor: {moeda_valor}')
print(argumento)
print(f'Tamanho: {len(argumento)}')