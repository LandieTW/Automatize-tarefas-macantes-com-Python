"""
PROJETO: RENOMEANDO ARQUIVOS COM DATAS EM ESTILO AMERICANO PARA DATAS EM ESTILO EUROPEU

Suponha que seu chefe envie milhares de arquivos a você por email com datas em estilo americano (MM-DD-AAAA) nos nomes dos arquivos e precise que
eles sejam renomeados com datas em estilo europeu (DD-MM-AAAA). 
Essa tarefa maçante poderia exigir um dia inteiro para ser feita manualmente!
Vamos criar um programa para fazer isso.

Eis o que o programa deve fazer:

    • Procurar todos os nomes de arquivo no diretório de trabalho atual em busca de datas em estilo americano.
    • Quando um arquivo for encontrado, ele deverá ser renomeado com o mês e o dia trocados para deixar a data em estilo europeu.

Isso significa que o código deverá fazer o seguinte:

    • Criar uma regex que possa identificar o padrão de texto para datas em estilo americano.
    • Chamar os.listdir() para encontrar todos os arquivos no diretório de trabalho.
    • Percorrer todos os nomes de arquivo em um loop usando a regex para verificar se ele contém uma data.
    • Se houver uma data, o arquivo deverá ser renomeado com shutil.move().
"""

#! python3
# renameDates.py – Renomeia os nomes de arquivo com formato de data MM-DD-AAAA em estilo
# americano para o formato DD-MM-AAAA em estilo europeu.

import shutil, os, re

# Cria uma regex que corresponda aos arquivos com formato de data em estilo americano.

nome_arquivo = re.compile(r"""^(.*?)        # todo o texto antes da data
    (d{2}?)-                                # um ou dois dígitos para o mês
    (d{1}?|d{2}?)                           # um ou dois dígitos para o dia
    (d{2}?|d{4}?)                           # dois ou quatro dígitos para o ano
    (.*?)$                                  # todo o texto após a data
""", re.VERBOSE)

# Percorre os arquivos do diretório de trabalho com um loop.
for arquivo_americano in os.listdir('.'):
    mo = nome_arquivo.search(arquivo_americano)
# Ignora os arquivos que não tenham uma data.
    if mo == None:
        continue
# Obtém as diferentes partes do nome do arquivo.
    antes_data = mo.group(1)
    mes = mo.group(2)
    dia = mo.group(4)
    ano = mo.group(6)
    depois_data = mo.group(8)
# Compõe o nome do arquivo em estilo europeu.
    arquivo_europeu = antes_data + dia + '-' + mes + '-' + ano + depois_data
# Obtém os paths absolutos completos dos arquivos.
    caminho = os.path.abspath('.')
    arquivo_americano = os.path.join(caminho, arquivo_americano)
    arquivo_europeu = os.path.join(caminho, arquivo_europeu)
# Renomeia os arquivos.
    print('Renaming "%s" to "%s"...' % (arquivo_americano, arquivo_europeu))

shutil.move(arquivo_americano, arquivo_europeu) # remova o caractere de comentário após os testes
