usuarios = {
    "ruan": "25",
    "cinthia": "25",
    "nayara": "42"
}

for nome, idade in usuarios.items():
    print(f'Nome: {nome.title()}, Idade: {idade}')

print("##")
print(usuarios.get("Neymar", "Usuário não encontrado"))
