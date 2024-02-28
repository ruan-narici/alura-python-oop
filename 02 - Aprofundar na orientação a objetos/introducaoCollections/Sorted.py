lista_numeros = [1,4,5,6,2,3,8,9,7,0]

lista_ordenada_crescente = sorted(lista_numeros)
lista_ordenada_decrescente = sorted(lista_numeros, reverse=True)

lista_numeros.sort() # Ordenando a propria lista

print(f'Crescente: {lista_ordenada_crescente}')
print(f'Decrescente: {lista_ordenada_decrescente}')
print(f'Propria lista: {lista_numeros}')
