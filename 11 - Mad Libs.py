"""
MAD LIBS

Crie um programa Mad Libs que leia arquivos-texto e permita que o usuário acrescente seus próprios textos em qualquer local em que a palavra
ADJECTIVE, NOUN, ADVERB ou VERB aparecer no arquivo-texto. 
Por exemplo, um arquivo-texto poderá ter o seguinte aspecto:

"The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events."

O programa deve localizar essas ocorrências e pedir que o usuário as substitua.

Enter an adjective:
    "silly"

Enter a noun:
    "chandelier"

Enter a verb:
    "screamed"

Enter a noun:
    "pickup truck"

O texto a seguir deverá ser criado:
    "The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events."

O resultado deverá ser exibido na tela e salvado em um novo arquivo-texto.
"""


from csv import writer


with open("teste.txt") as arquivo:
    dados = arquivo.read()
    lista_dados = dados.split(" ")

    adjetivo = input("Insira um adjetivo: ")
    nome = input("Insira um nome: ")
    verbo = input("Insira um verbo: ")
    nome2 = input("Insira mais um nome: ")

    for i in lista_dados:
        if i == "ADJECTIVE":
            i = adjetivo
        elif i == "NOUN":
            i = nome
        elif i == "VERB":
            i = verbo
        elif i == "NOUN":
            i = nome2
    
    dados_tratados = " ".join(lista_dados)

    with open("teste2.txt", "w") as novo_arquivo:
        dados = writer(novo_arquivo)
        dados.writerow(dados_tratados)
