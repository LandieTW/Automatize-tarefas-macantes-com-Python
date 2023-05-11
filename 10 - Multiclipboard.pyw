"""
MULTICLIPBOARD
"""


# ! python3


# Como utilizar a partir do prompt de comando:                      python 10Multiclipboard.pyw save <palavra-chave>
# Como deletar a partir do prompt de comando:                       python 10Multiclipboard.pyw delete <palavra-chave>
# Como deletar tudo a partir do prompt de comando:                  python 10Multiclipboard.pyw deleteall
# Como carregar a palavra-chave no clipboard:                       python 10Multiclipboard.pyw <palavra-chave>
# Como carregar todas as palavras-chaves no clipboard:              python 10Multiclipboard.pyw list


import shelve
import pyperclip
import sys


multiclipboard = shelve.open('10Multiclipboard.pyw')


if len(sys.argv[0]) == 20 and sys.argv[1].lower() == 'save':
    multiclipboard[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:                                        # entrada: 10Multiclipboard.pyw <palavra-chave> ou 10Multiclipboard.pyw list (2 elementos)
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(multiclipboard.keys())))
    elif sys.argv[1].lower() == 'delete':
        del multiclipboard[sys.argv[2]]                             # deleta o item da chave informada.
    elif sys.argv[1].lower() == 'deleteall':
        for key in multiclipboard:
            del multiclipboard[key]                                 # deleta todos os itens do shelve file
    elif sys.argv[1] in multiclipboard:
        pyperclip.copy(multiclipboard[sys.argv[1]])
multiclipboard.close()
