

class ExtratorURL:

    def __init__(self, url: str):
        if self.url_valida(url):
            self._url = url.lower()
        else:
            raise LookupError("URL inválida!")

    def url_valida(self, url: str) -> bool:
        if url and url.startswith("https://www.bytebank.com"):
            return True
        else:
            return False

    def extrair_valores(self) -> list:
        querys = self._url.split("?")[1]
        parametros = querys.split("&")
        valor = list()
        for parametro in parametros:
            parametro_quebrado = parametro.split("=")
            valor.append(parametro_quebrado[1])
        return valor

    def __str__(self):
        moeda_origem, moeda_destino, moeda_valor = self.extrair_valores()
        return f'Moeda origem: {moeda_origem}, Moeda destino: {moeda_destino}, Valor: {moeda_valor}'

    def __len__(self):
        return len(self._url)
