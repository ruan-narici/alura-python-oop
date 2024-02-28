from Filme import Filme
from Serie import Serie
from Playlist import Playlist

filme1 = Filme('Predestinado', 2022, 97)
filme2 = Filme('A Colónia', 2021, 204)
serie1 = Serie('1899', 2022, 1)
serie2 = Serie('Peaky Blinders', 2013, 6)

filmes_e_series = [filme1, filme2, serie1, serie2]

# for programa in filmes_e_series:
#    print(programa)

playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
    print(programa)
