"""
INVENTÁRIO DE UM JOGO DE FANTASIA

Você cria um videogame de fantasia.
A estrutura de dados para modelar o inventário do jogador será um dicionário em que as chaves são valores de string que
descrevem o item do inventário e o valor será um inteiro detalhando quantos itens desse tipo o jogador tem.
Por exemplo, o valor de dicionário {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} quer dizer que o jogador
tem 1 corda (rope), 6 tochas (torches), 42 moedas de ouro (gold coins) e assim por diante.

Crie uma função chamada displayInventory() que possa receber qualquer “inventário” possível e exiba essas informações
da seguinte maneira:

Inventory:
    12 arrow
    42 gold coin
    1 rope
    6 torch
    1 dagger
    Total number of items: 62

FUNÇÃO DE 'LISTA PARA DICIONÁRIO' PARA O INVENTÁRIO DE JOGO DE FANTASIA

Suponha que os despojos de um dragão vencido seja representado como uma lista de strings como esta:
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Crie uma função chamada addToInventory(inventory, addedItems), em que o parâmetro inventory seja um dicionário
representando o inventário do jogador (como no projeto anterior) e o parâmetro addedItems seja uma lista como
dragonLoot.
A função addToInventory() deve retornar um dicionário que represente o inventário atualizado.
Observe que a lista addedItems pode conter vários itens iguais.
"""


inventario1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayinventory(inventario: dict) -> None:
    try:
        soma = 0
        for chave, valor in inventario.items():
            soma += valor
            print(f'{valor} {chave}')
        print(f'Total number of itens: {soma}')
    except KeyError:
        raise 'Erro de chave inexistente'


def addtoinventory(inventario: dict, itens_adicionados: list) -> None:
    for i in itens_adicionados:
        if i in inventario:
            inventario[i] += 1
        else:
            inventario[i] = 1


displayinventory(inventario1)
addtoinventory(inventario1, dragon_loot)
displayinventory(inventario1)
