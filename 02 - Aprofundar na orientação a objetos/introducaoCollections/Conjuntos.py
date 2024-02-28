lista_id_alunos_eletronica = [25, 12, 23, 54, 32]
lista_id_alunos_iot = [25, 24, 20, 32, 78]


# Serão salvos dados repetidos.
lista_assistiram = []
lista_assistiram.extend(lista_id_alunos_eletronica)
lista_assistiram.extend(lista_id_alunos_iot)
print(lista_assistiram)

## Usando set para evitar a repetição, porém não temos index e nem ordem
lista_assistiram = set(lista_assistiram)
print(lista_assistiram)

## Verificando quem fez iot e não fez eletronica
fez_iot_mas_nao_eletronica = set(lista_id_alunos_iot) - set(lista_id_alunos_eletronica)
print(fez_iot_mas_nao_eletronica)

## Verificando quem fez eletronica ou iot separadamente. Ou seja, nao pode ter feito os dois
fez_iot_ou_eletronica = set(lista_id_alunos_iot) ^ set(lista_id_alunos_eletronica)
print(fez_iot_ou_eletronica)

