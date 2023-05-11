"""
GERANDO ARQUIVOS ALEATÓRIOS DE PROVAS

Suponha que você seja um professor de geografia, tenha 35 alunos na sua classe e queira aplicar uma prova surpresa
sobre as capitais dos estados norteamericanos.
Infelizmente, a sua classe tem alguns alunos desonestos, e não é possível confiar neles acreditando que não vão colar.
Você gostaria de deixar a ordem das perguntas aleatória para que cada prova seja única, fazendo com que seja impossível
para alguém copiar as respostas de outra pessoa.
É claro que fazer isso manualmente seria uma tarefa demorada e maçante.
Felizmente, você conhece um pouco de Python.

Eis o que o programa faz:
• Cria 35 provas diferentes.
• Cria 50 perguntas de múltipla escolha para cada prova em ordem aleatória.
• Fornece a resposta correta e três respostas incorretas aleatórias para cada pergunta em ordem aleatória.
• Grava as provas em 35 arquivos-texto.
• Grava os gabaritos contendo as respostas em 35 arquivos-texto.

Isso significa que o código deverá fazer o seguinte:
• Armazenar os estados e as suas capitais num dicionário.
• Chamar open(), write() e close() para os arquivos-texto contendo as provas e os gabaritos com as respostas.
• Usar random.shuffle() para deixar a ordem das perguntas e as opções de múltipla escolha aleatórias.

PASSO 1: ARMAZENAR OS DADOS DA PROVA EM UM DICIONÁRIO

PASSO 2: CRIAR O ARQUIVO COM A PROVA E EMBARALHAR A ORDEM DAS PERGUNTAS

A prova deve ter um nome único de arquivo e deve também ter algum tipo de cabeçalho padrão, com espaços
para o aluno preencher o nome, a data e o período da classe.

Os nomes dos arquivos para as provas serão capitalsquiz<N>.txt, em que <N> é um número único para
a prova, proveniente de quizNum, o contador do loop for.
O gabarito das respostas de capitalsquiz<N>.txt será armazenado num arquivo-texto chamado
capitalsquiz_answers<N>.txt.

PASSO 3: CRIAR AS OPÇÕES DE RESPOSTA

Agora devemos gerar as opções de resposta para cada pergunta, que corresponderão às múltiplas escolhas de A até D.
Criar também as 35 listas gabaritos e as 105 listas de respostas corretas.

PASSO 4: GRAVAR CONTEÚDO NOS ARQUIVOS DE PROVA E DE RESPOSTAS

Nome completo:
Data:
Período:
Quiz - Capital de cada estado (Formulário <número da prova>)

1. Qual a capital do(a) West Virginia?
A. Hartford
B. Santa Fe
C. Harrisburg
D. Charleston

2. Qual a capital do(a) Colorado?
A. Raleigh
B. Harrisburg
C. Denver
D. Lincoln

...

O arquivo gabarito:
1. D
2. C
3. A
4. C
"""

# ! python3

from random import shuffle, randint
from csv import writer

capitais = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
            'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
            'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


class Prova:

    def __init__(self, numero_de_questoes: int = 35) -> None:
        self.__numero_de_questoes = numero_de_questoes


    @staticmethod
    def criarprovas(numero_de_questoes: int = 35) -> None:

        for numero in range(1, numero_de_questoes + 1):

            with open(f"Prova {numero}.txt", 'w') as prova:
                cabecalho = writer(prova)
                cabecalho_lista = [
                    'Nome completo: \n'
                    'Data: \n'
                    'Período: \n'
                    f'Quiz - Capital de cada estado (Formulário {numero}) \n'
                ]
                cabecalho.writerow(cabecalho_lista)

                string = ""

                numero_questao = 0

                chaves_embaralhadas = list(capitais.keys())
                shuffle(chaves_embaralhadas)
                dicionario_embaralhado = {}
                for i in range(len(chaves_embaralhadas)):
                    dicionario_embaralhado[chaves_embaralhadas[i]] = capitais[chaves_embaralhadas[i]]

                for chave, valor in dicionario_embaralhado.items():

                    opcoes = [
                        valor,
                        dicionario_embaralhado[chaves_embaralhadas[randint(0, 49)]],
                        dicionario_embaralhado[chaves_embaralhadas[randint(0, 49)]],
                        dicionario_embaralhado[chaves_embaralhadas[randint(0, 49)]]
                    ]
                    shuffle(opcoes)
                    a = opcoes[0]
                    b = opcoes[1]
                    c = opcoes[2]
                    d = opcoes[3]

                    numero_questao += 1

                    questoes = writer(prova)
                    questoes_lista = [
                        f"{numero_questao}. Qual a capital do(a) {chave}? \n"
                        f"A. {str(a)} \n"
                        f"B. {str(b)} \n"
                        f"C. {str(c)} \n"
                        f"D. {str(d)} \n"
                    ]
                    questoes.writerow(questoes_lista)

                    if valor == a:
                        letra = "A"
                    elif valor == b:
                        letra = "B"
                    elif valor == c:
                        letra = "C"
                    else:
                        letra = "D"
                    string += f"{numero_questao}.{letra}\n"

                    gabarito = string.splitlines()

                    with open(f"Prova {numero} (Gabarito).txt", 'w') as prova_gabarito:
                        respostas = writer(prova_gabarito, delimiter="\n")
                        respostas.writerow(gabarito)


Prova.criarprovas(35)
