from datetime import date, datetime, timezone, timedelta


data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
print(data_em_texto)

data_hora_atual = datetime.now()
data_hora_em_texto = data_hora_atual.strftime('%d/%m/%Y %H:%M')
print(data_hora_em_texto)

data_hora_em_texto = '20/02/2024 11:00'
data_hora_convertida = datetime.strptime(data_hora_em_texto, '%d/%m/%Y %H:%M')
print(data_hora_convertida)

diferenca = timedelta(hours=-3)
fuso_horario = timezone(diferenca)
print(fuso_horario)

data_hora_sao_paulo = data_hora_convertida.astimezone(fuso_horario)
data_hora_sao_paulo_em_texto = data_hora_sao_paulo.strftime('%d/%m/%Y %H:%M')
print(data_hora_sao_paulo_em_texto)
