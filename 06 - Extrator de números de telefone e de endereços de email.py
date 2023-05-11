"""
EXTRATOR DE NÚMEROS DE TELEFONE E DE ENDEREÇOS DE E-MAIL

Problema proposto:
Suponha que você tenha a tarefa maçante de localizar todos os números de telefone e endereços de email em uma página web ou um documento extenso.
Se fizer rolagens manualmente pela página, você poderá acabar fazendo a pesquisa por bastante tempo.

Solução:
Porém, se você tivesse um programa que pudesse pesquisar o texto em seu clipboard em busca de números de telefone e de endereços de email,
seria possível simplesmente pressionar CTRL-A para selecionar todo o texto, CTRL-C para copiá-lo para o clipboard e então executar o seu programa.

Ele poderia substituir o texto no clipboard somente pelos números de telefone e pelos endereços de email encontrados.
Por exemplo, seu extrator de números de telefone e de endereços de email deverá fazer o seguinte:
    • Obter o texto do clipboard.
    • Encontrar todos os números de telefone e os endereços de email no texto.
    • Colá-los no clipboard.

Agora você poderá começar a pensar em como isso funcionará no código. O código deverá fazer o seguinte:
    • Usar o módulo pyperclip para copiar e colar strings.
    • Criar duas regexes: uma para corresponder a números de telefone e outra para endereços de email.
    • Encontrar todas as correspondências, e não apenas a primeira, para ambas as regexes.
    • Formatar as strings correspondentes de forma elegante em uma única string a ser colada no clipboard.
    • Exibir algum tipo de mensagem caso nenhuma correspondência tenha sido encontrada no texto.

PASSO 1: CRIAR UMA REGEX PARA NÚMEROS DE TELEFONE

O número de telefone começa com um código de área opcional, portanto o grupo para código de área é seguido de um ponto de interrogação.
Formato de telefone BR: +55 XX 9XXXX-XXXX

PASSO 2: CRIAR UMA REGEX PARA ENDEREÇOS DE E-MAIL

Também será necessário ter uma expressão regular que possa corresponder a endereços de email.
A parte referente ao nome do usuário no endereço de email "u" tem um ou mais caracteres que podem ser: [a-z A-Z 0-9 ._%+-].
O domínio e o nome do usuário são separados por um símbolo de @ "v".
O nome de domínio "w" tem uma classe de caracteres um pouco menos permissiva, contendo apenas letras, números, pontos e hifens: [a-z A-Z 0-9 .-].
Por fim, temos a parte “.com” que, na verdade, pode ser um ponto seguido de qualquer caractere.

PASSO 3: ENCONTRAR TODAS AS CORRESPONDÊNCIAS NO TEXTO DO CLIPBOARD

O módulo re localiza todas as correspondências no clipboard.
A função pyperclip.paste() obtém um valor de string com o texto que está no clipboard.
O método regex findall() retornará uma lista de tuplas.
Há uma tupla para cada correspondência e cada tupla contém strings para cada grupo da expressão regular.
Lembre-se de que o grupo 0 corresponde à expressão regular completa, portanto o grupo no índice 0 da tupla é aquele em que estaremos interessados.
Como podemos ver em u, as correspondências serão armazenadas em uma variável de lista chamada matches.
O programa começa com uma lista vazia e dois loops for.
Para os endereços de email, devemos concatenar o grupo 0 de cada correspondência w.
Para os números de telefone correspondentes, não queremos concatenar somente o grupo 0.
Embora o programa detecte números de telefone em diversos formatos, queremos que esse número seja concatenado em um formato único e padrão.
A variável phoneNum contém uma string criada a partir dos grupos 1, 3, 5 e 8 do texto correspondente v.

PASSO 4: REUNIR AS CORRESPONDÊNCIAS EM UMA STRING PARA O CLIPBOARD

Agora que temos os endereços de email e os números de telefone na forma de uma lista de strings em matches, devemos inseri-los no clipboard.
A função pyperclip.copy() aceita apenas um único valor de string, e não uma lista de strings; sendo assim, você deve chamar o método join() em matches.
Se nenhum número de telefone ou endereço de email for encontrado, o programa deverá informar isso ao usuário.
"""

"""
+55 21 98004-7240
+55 24 95863-9900
+55 72 94153-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
"""


# ! python3

import pyperclip as ppc
import re

telefones: str = re.compile(r'''
    \+55       # código do país
    \s         # espaço em branco
    \d{2}      # código de área
    \s         # espaço em branco
    9          # número do celular
    \d{4}      # quatro primeiros dígitos do número
    -?         # traço
    \d{4}      # quatro últimos dígitos do número
    ''', re.VERBOSE)

email: str = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  # Parte local do endereço de e-mail, pode conter letras, números, pontos, underscores, porcentagens e sinais de mais e menos.
    @                  # Símbolo "@" que separa a parte local do domínio.
    [a-zA-Z0-9.-]+     # Domínio do endereço de e-mail, pode conter letras, números, pontos e traços.
    (\.[a-zA-Z]{2,4})    # Extensão do domínio, que deve conter um ponto seguido de 2 a 4 letras.
)''', re.VERBOSE)

texto: str = str(ppc.paste())   # cria uma variável com todas as informações copiadas inicialmente (na forma de string, para ser vasculhada pelo ppc.findall)
lista: list = []

for elemento in telefones.findall(texto):   # findall procura todas as ocorrências de um dado dentro de uma string
    numero_telefone = ' '.join([elemento[0:17]])
    lista.append(numero_telefone)

for elemento in email.findall(texto):   # findall procura todas as ocorrências de um dado dentro de uma string
    lista.append(elemento[0])

if len(lista) > 0:                  # se achar alguma ocorrência...
    ppc.copy('\n'.join(lista))
    print('Copiado:')
    print('\n'.join(lista))

else:
    print('Nenhum telefone/email encontrado(s).')
