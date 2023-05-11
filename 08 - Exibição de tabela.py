"""
EXIBIÇÃO DE TABELA

Crie uma função chamada printTable() que receba uma lista de listas de strings e a 
exiba em uma tabela bem organizada, com cada coluna justificada à direita. 
Suponha que todas as listas internas contenham o mesmo número de strings. 
Por exemplo, o valor poderá ter o seguinte aspecto:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]

Sua função printTable() exibirá o seguinte:

    apples Alice dogs
    oranges Bob cats
    cherries Carol moose
    banana David goose

Dica: seu código inicialmente deverá localizar a string mais longa em cada uma das listas 
internas para que a coluna toda tenha largura suficiente para que todas as strings possam 
ser inseridas. 
Você pode armazenar a largura máxima de cada coluna como uma lista de inteiros. 
A função printTable() pode começar com colWidths = [0] * len(tableData), que criará uma 
lista contendo o mesmo número de valores 0 que o número de listas internas em tableData. 
Dessa maneira, colWidths[0] poderá armazenar a largura da string mais longa de tableData[0], 
colWidths[1] poderá armazenar a largura da string mais longa de tableData[1] e assim por diante. 
Você poderá então identificar o maior valor na lista colWidths e descobrir a largura na forma de
um inteiro a ser passada para o método de string rjust().
"""


tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]
tableData2 = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']]



def print_table(lista: list) -> str:

    referencia = []
    lista_auxiliar = []

    for j in range(len(lista)):

        referencia.append(len(lista[j]))

        for k in range(len(lista[j])):

            lista_auxiliar.append(lista[j][k])
    
    for i in range(1, len(referencia)):

        lista_auxiliar.insert(referencia[i - 1] * i + (i - 1), '\n')
    
    string = ' '.join(lista_auxiliar)

    return string


print(print_table(tableData))
print(print_table(tableData2))
