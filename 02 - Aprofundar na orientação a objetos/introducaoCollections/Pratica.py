from collections import Counter

texto1 = """
O documento de contratação da empresa responsável pela funcionária Sandra de Souza Marinho — que caiu ao limpar o toldo de uma escola pública no Distrito Federal — previa a limpeza mensal das calhas do telhado do local. O pregão eletrônico ainda especificava o uso de escada, quando necessário, com equipamentos apropriados fornecidos pela empresa contratada (veja foto abaixo).

✅ Clique aqui para seguir o canal do g1 DF no WhatsApp.

No entanto, a empresa Real Jg Facílitis negou que tinha conhecimento dessa função exercida pela funcionária envolvendo altura. Sandra de Souza, de 41 anos, trabalha na Escola Classe 10, em Ceilândia, como auxiliar de serviços gerais há 7 anos. Ela está internada em estado grave no Hospital de Base.
O caso é investigado pela Polícia Civil e pela Corregedoria da Secretaria de Educação. Procurada pela TV Globo, a empresa respondeu que, apesar do contrato prever limpeza de calhas, a funcionária não era capacitada para esse trabalho e que não estava sob ordens da empresa.

A empresa informou ainda que está em contato com a família de Sandra para prestar todo o apoio necessário.

Segundo a Real Jg Facílitis, foram fornecidos à funcionária os equipamentos de proteção compatíveis com a função dela, de conservação e limpeza — como bota e luvas. Mas não equipamentos para trabalho em altura porque, em nenhuma hipótese, ela ou outros funcionários deveriam fazer esse tipo de trabalho, principalmente usando uma escada (veja detalhes mais abaixo).
Imagens da câmera de segurança do colégio público mostram o momento da queda de Sandra, na última sexta-feira (16), quando ela limpava o toldo de entrada da escola (veja vídeo acima).

As imagens mostram a funcionária em cima de uma escada limpando o toldo com um jato de água. Após alguns segundos, a escada desliza no chão molhado e Sandra cai de uma altura de aproximadamente 4 metros.

A mulher bateu a cabeça e sofreu convulsões. Ela foi levada para o Hospital de Base onde permanece internada em estado grave. A família registrou um boletim de ocorrência na Polícia Civil.
"""

def frequencia_aparicao(texto: str):
    aparicoes = Counter(texto.lower())
    total_aparicoes = sum(aparicoes.values())
    proporcao = [(letra, quantidade / total_aparicoes * 100) for letra, quantidade in aparicoes.items()]
    porporcao_ordenada = Counter(dict(proporcao))
    mais_comuns = porporcao_ordenada.most_common(10)
    return mais_comuns

aparicoes = frequencia_aparicao(texto1)
print(aparicoes)
