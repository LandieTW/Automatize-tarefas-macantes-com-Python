"""
ADICIONANDO MARCADORES NA MARCAÇÃO DA WIKI

Ao editar um artigo na Wikipedia, podemos criar uma lista com marcações (bullets) ao inserir cada item da 
lista em sua própria linha e inserindo um asterisco na frente. 
Porém suponha que você tenha uma lista realmente extensa em que você queira acrescentar marcadores.

O script bulletPointAdder.py obterá o texto do clipboard, adicionará um asterisco e um espaço no início de 
cada linha e, em seguida, colará esse novo texto no clipboard. 
Por exemplo, se eu copiar o texto a seguir [do artigo “List of Lists of Lists” (Listas de listas de listas) 
da Wikipedia] para o clipboard:

    Lists of animals
    Lists of aquarium life
    Lists of biologists by author abbreviation
    Lists of cultivars

e depois executar o programa bulletPointAdder.py, o clipboard conterá o seguinte:

    * Lists of animals
    * Lists of aquarium life
    * Lists of biologists by author abbreviation
    * Lists of cultivars

Esse texto contendo um asterisco como prefixo está pronto para ser colado em um artigo da Wikipedia como uma lista com marcadores.

PASSO 1: COPIAR E COLAR NO CLIPBOARD

Queremos que o programa bulletPointAdder.py faça o seguinte:

    1. Obtenha o texto do clipboard.
    2. Faça algo com ele.
    3. Copie o novo texto para o clipboard.

PASSO 2: SEPARAR AS LINHAS DE TEXTO E ACRESCENTAR O ASTERÍSTICO

PASSO 3: JUNTAR AS LINHAS MODIFICADAS
"""


import pyperclip as ppc


texto = ppc.paste()

lista = texto.split('\n')

for i in range(len(lista)):
    lista[i] = '* ' + str(lista[i])

texto = '\n'.join(lista)

ppc.copy(texto)
