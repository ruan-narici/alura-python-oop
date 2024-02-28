from datetime import datetime, timedelta


class DataHoraBr:

    def __init__(self):
        self.data_registro = datetime.now()

    def __str__(self):
        return self.formatar()

    def momento_registro(self):
        return self.data_registro

    def mes(self):
        meses = [
            'Janeiro', 'Fevereiro', "Março", 'Abril',
            'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        return meses[self.momento_registro().month - 1]


    def dia(self):
        dias = [
            'Segunda-feira', 'Terça-feira', 'Quarta-feira',
            'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo'
        ]
        return dias[self.momento_registro().weekday()]

    def formatar(self):
        return self.momento_registro().strftime('%d/%m/%Y %H:%M:%S')

    def tempo_cadastrado(self):
        return (datetime.now() + timedelta(days=1)) - self.data_registro
