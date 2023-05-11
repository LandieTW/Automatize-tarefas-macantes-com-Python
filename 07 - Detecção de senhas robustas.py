"""
DETECÇÃO DE SENHAS ROBUSTAS

Crie uma função que utilize expressões regulares para garantir que a string de senha recebida seja robusta. 
Uma senha robusta deve ter pelo menos oito caracteres, deve conter tanto letras maiúsculas quanto letras minúsculas e ter pelo menos um dígito. 
Talvez seja necessário testar a string em relação a diversos padrões de regex para validar sua robustez.

Crie uma função que receba uma string e faça o mesmo que o método de string strip(). 
Se nenhum outro argumento for passado além da string em que a remoção será feita, os caracteres de espaço em branco serão removidos do início e do fim da string. 
Caso contrário, os caracteres especificados no segundo argumento da função serão removidos da string.
"""

import re

def deteccao_de_senhas_robustas(senha: str) -> str:

    senha_robusta_letra_maiuscula: str = re.compile(r'''
        [A-Z]  # Elementos que devem ser verificados se estão presentes na senha
    ''', re.VERBOSE)
    senha_robusta_letra_minuscula: str = re.compile(r'''
        [a-z]  # Elementos que devem ser verificados se estão presentes na senha
    ''', re.VERBOSE)
    senha_robusta_digito: str = re.compile(r'''
        [0-9]  # Elementos que devem ser verificados se estão presentes na senha
    ''', re.VERBOSE)

    if len(senha) < 8:
        print(f"Sua senha tem apenas {len(senha)} elementos.\nO mínimo são 8, portanto, sua senha é fraca.")
    else:
        lista_digito = []
        lista_maiuscula = []
        lista_minuscula = []
        for digito in senha_robusta_digito.findall(senha):
            lista_digito.append(digito)
        for maiuscula in senha_robusta_letra_maiuscula.findall(senha):
            lista_maiuscula.append(maiuscula)
        for minuscula in senha_robusta_letra_minuscula.findall(senha):
            lista_minuscula.append(minuscula)
        if len(lista_digito) == 0:
            return f'Sua senha, {senha}, não possui dígitos, portanto, sua senha é fraca.'
        elif len(lista_maiuscula) == 0:
            return f'Sua senha, {senha}, não possui letras maiúsculas, portanto, sua senha é fraca.'
        elif len(lista_minuscula) == 0:
            return f'Sua senha, {senha}, não possui letras minúsculas, portanto, sua senha é fraca.'
        else:
            return f'Sua senha, {senha}, é robusta.'

print(deteccao_de_senhas_robustas(x := input("Qual a senha a ser verificada?")))
