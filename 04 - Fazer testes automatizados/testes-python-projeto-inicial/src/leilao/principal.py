from dominio import Leilao, Lance, Usuario, Avaliador

usr_ruan = Usuario("Ruan")
usr_cinthia = Usuario("Cinthia")

celular_leilao = Leilao("Celular Iphone 14")

primeiro_lance = Lance(usr_ruan, 3000.0)
segundo_lance = Lance(usr_cinthia, 3300.0)

celular_leilao.guardar_lance(primeiro_lance)
celular_leilao.guardar_lance(segundo_lance)

for lance in celular_leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu o lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avaliar(celular_leilao.lances)
print(f'O menor lance foi R$ {avaliador.menor_valor} e o maior foi R$ {avaliador.maior_valor}')
