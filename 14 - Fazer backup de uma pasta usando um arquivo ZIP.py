"""
FAZER BACKUP DE UMA PASTA USANDO UM ARQUIVO ZIP

Suponha que você esteja trabalhando em um projeto cujos arquivos são mantidos em uma pasta chamada C:\Livro_Python. 
Você está preocupado em perder seu trabalho, portanto gostaria de criar arquivos ZIP que sejam “snapshots” (imagens instantâneas) de toda a pasta. 
Você gostaria de manter diferentes versões, portanto quer que o nome dos arquivos ZIP seja incrementado a cada vez que for criado; por exemplo, 
Livro_Python_1.zip, Livro_Python_2.zip, Livro_Python_3.zip e assim por diante. 
Isso poderia ser feito manualmente, porém é uma tarefa irritante e você poderia acidentalmente usar um número incorreto nos nomes dos arquivos ZIP. 
Será muito mais simples executar um programa que realize essa tarefa maçante para você.
Para esse projeto, abra uma nova janela no editor de arquivo e salve o programa como backupToZip.py.
"""

#! python3


import zipfile, os


def backup_Zip(pasta):
    """Faz backup de todo o conteúdo de "folder" em um arquivo ZIP."""
    pasta = os.path.abspath(pasta)      # garante que folder é um path absoluto
    # Determina o nome do arquivo que esse código deverá usar de acordo com os arquivos já existentes.
    numero = 1
    while True:
        nome = os.path.basename(pasta) + '_' + str(numero) + '.zip'
        if not os.path.exists(nome):
            break
        numero += 1
    # Cria o arquivo ZIP.
    print('Criando %s...' % (nome))
    backupZip = zipfile.ZipFile(nome, 'w')
    # Percorre toda a árvore de diretório e compacta os arquivos de cada pasta.
    for nome_pasta, subfolders, nome_arquivos in os.walk(pasta):
        print('Adicionando arquivos em %s...' % (nome_pasta))
        # Acrescenta a pasta atual ao arquivo ZIP.
        backupZip.write(nome_pasta)
        # Acrescenta todos os arquivos dessa pasta ao arquivo ZIP.
        for nome_arquivo in nome_arquivos:
            base = os.path.basename(pasta) + '_'
            if nome_arquivo.startswith(base) and nome_arquivo.endswith('.zip'):
                continue        # não faz backup dos arquivos ZIP de backup
            backupZip.write(os.path.join(nome_pasta, nome_arquivo))
    backupZip.close()
    print('Concluído.')
backup_Zip('C:\\backup')
