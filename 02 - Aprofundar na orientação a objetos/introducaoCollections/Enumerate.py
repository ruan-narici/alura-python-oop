usuarios = [
    ("ruan", 1998, 25),
    ("cinthia", 1998, 25),
    ("nayara", 1982, 42)
]

for nome, _, idade in usuarios: # Ignorando um dado na lista
    print(nome, idade)


lista_idades = [25, 25, 42]
lista_idades_enumeradas = list(enumerate(lista_idades)) #Enumerando a lista

for i, idade in lista_idades_enumeradas:
    print(f'Indice: {i} - Idade: {idade}')
