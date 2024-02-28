idade1 = 25
idade2 = 26
idade3 = 42
idade4 = 17

idades = [idade1, idade2, idade3, idade4]

menor_de_idade = [(f"Idade: {idade}") for idade in idades if idade < 18]
maior_de_idade = [(f"Idade: {idade}") for idade in idades if idade >= 18]

print(menor_de_idade)
print(maior_de_idade)
