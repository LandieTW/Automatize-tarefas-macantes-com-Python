"""
SEQUÊNCIA DE COLLATZ:

Função com parâmetro de nome number.
Se number for par, collatz() deverá exibir number // 2 e retornar essse valor
Se number for ímpar, collatz() deverá exibir e retornar 3 * number + 1

Depois, o utilizador deve conseguir digitar um inteiro e ficar a chamar collatz() com esse número até a função
retornar o valor 1.

VALIDAÇÃO DE DADOS DE ENTRADA:

Acrescentar instruções try e except no projeto, para detetar se o utilizador digitou uma string que não corresponda a
um inteiro."""


def collatz(y: int) -> int | None:
    """Função que reproduz o comportamento da sequência de Collatz"""

    try:

        y = int(y)        # Converte para inteiro

        if y != 1 and y % 2:      # Condição: Se o número for ímpar, diferente de 1
            print(f'3 * {y} + 1 = {3 * y + 1}')
            return collatz(3 * y + 1)
        
        elif y != 1 and not y % 2:        # Condição: Se o número for par
            print(f'{y} // 2 = {y // 2}')
            return collatz(y // 2)
        
        else:       # Condição: Se o número for 1
            return print(y)
        
    except ValueError:
        z = int(input('O valor, que você digitou, não é um inteiro. Por favor, tente novamente.'))
        return collatz(z)
    
    except RecursionError:
        z = int(input('O valor deve ser maior do que 0. Por favor, tente novamente.'))
        return collatz(z)


n = int(input('Digite um número por favor'))


collatz(n)
