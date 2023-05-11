"""
PESQUISA COM REGEX

Crie um programa que abra todos os arquivos .txt de uma pasta e procure todas as linhas que correspondam a uma expressão regular fornecida pelo
usuário. O resultado deverá ser exibido na tela.
"""


import os
from csv import reader


diretorio = "C:\\Users\\daniel.wanderley\\Downloads\\Meus cursos\\Meus projetos\\teste"


for nome_arquivo in os.listdir(diretorio):                          # coloca os arquivos presentes no caminho na forma lista e itera 

    if nome_arquivo.endswith(".txt"):                               # se o arquivo é do tipo .txt

        caminho_completo = os.path.join(diretorio, nome_arquivo)    # completa o caminho, adicionando o arquivo .txt encontrado

        with open(caminho_completo, "r") as arquivo:                # abre o arquivo para leitura

            for linha in arquivo:

                lista_linha = linha.split(" ")

                if str(lista_linha[0]) == "CAPEX":                             # se o primeiro elemento contido na linha iterada for "CAPEX"

                    string_linha = " ".join(lista_linha) + "\n"

                    print(string_linha)                                    # printa a linha inteira do arquivo
