"""
CÓDIGO PARA VÍRGULAS

Função que aceite um valor de lsta como argumento e retorne uma string com todos os itens separados por uma vírgula e
um espaço, com 'and' inserido antes do último item.

A função deve conseguir trabalhar com qualquer valor de lista que ela receber.
"""


# Listas para testes:
lista1 = ['apples', 'bananas', 'tofu', 'cats']
lista2 = []
lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista4 = [1, 'apples', 2, 'bananas', 3, 'tofu', 4, 'cats', 5]
lista5 = [['apples', 'bananas', 'tofu', 'cats'], 'apples', 'bananas', 'tofu', 'cats']
lista6 = [['apples', 'bananas', 'tofu', ['apples', 'bananas', 'tofu', 'cats'], 'cats'], 'apples', 'bananas', 'tofu', 'cats']


def codigo_para_virgulas(lista: list) -> str:
    """Função que abre listas na forma de string"""
    try:

        for i in range(0, len(lista)):
            if type(lista[i]) == list:
                lista = abre_lista(lista, i)
                codigo_para_virgulas(lista)     # chama de novo a função, caso hajam sublistas ainda...

        string = ""
        for k in range(0, len(lista) - 2):      # transforma em str
            string += str(lista[k]) + ", "
        string += str(lista[-2]) + " and " + str(lista[-1])     # adiciona o termo aditivo entre os 2 últimos elementos

        return string

    except IndexError:
        return 'A lista está vazia'


def abre_lista(lista: list, i: int) -> list:
    """Função que abre sublistas"""

    sublista = []
    for j in range(0, len(lista[i])):       # reconstrói a sublista nos seus elementos
        sublista.append(lista[i][j])
    lista = lista[:i] + sublista + lista[(i + 1):]      # reconstrói a lista principal

    return lista


print(codigo_para_virgulas(lista1))
print(codigo_para_virgulas(lista2))
print(codigo_para_virgulas(lista3))
print(codigo_para_virgulas(lista4))
print(codigo_para_virgulas(lista5))
print(codigo_para_virgulas(lista6))
# print(codigo_para_virgulas(lista8))
