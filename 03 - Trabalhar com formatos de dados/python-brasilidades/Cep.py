import requests


class Cep:

    def __init__(self, cep):
        if self.valida(cep):
            self.cep = str(cep)
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.formata()

    def valida(self, cep):
        if len(str(cep)) == 8:
            return True
        else:
            return False

    def formata(self):
        cep_formatado = f'{self.cep[:5]}-{self.cep[5:]}'
        return cep_formatado

    def acessa_api_via_cep(self):
        proxies = {
            'http': 'http://lazaro.paixao:Teiu%402024%21@192.168.201.254:3128/',
            'https': 'http://lazaro.paixao:Teiu%402024%21@192.168.201.254:3128/'
        }
        url = f'https://viacep.com.br/ws/{self.cep}/json/'
        req = requests.get(url=url, proxies=proxies)
        res = req.json()
        return (
            res['bairro'],
            res['localidade'],
            res['uf']
        )
