import re


padrao_regex = "\\w{5,50}\\@\\w{5,10}\\.\\w{2,5}\\.\\w{2,3}"
primeiro_email = "asdiojasoida ruannarici@hotmail.com.br asoidjasoid"
segundo_email = "aiosdjaois sioadas @dasdas . com"

primeira_resposta = re.search(padrao_regex, primeiro_email)

print(primeira_resposta.group())