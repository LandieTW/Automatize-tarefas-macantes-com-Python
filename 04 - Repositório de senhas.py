"""
REPOSITÓRIO DE SENHAS

É provável que você tenha contas em vários sites diferentes.
Usar a mesma senha neles todos é um péssimo hábito porque, se um desses sites tiver uma falha de segurança,
os hackers saberão a senha de todas as suas demais contas.
É melhor usar um software gerenciador de senhas no seu computador que utilize uma senha principal para
desbloquear esse gerenciador de senhas.
Então você poderá copiar qualquer senha de conta para o clipboard e colá-la no campo de senha dos sites.
O programa gerenciador de senhas que criaremos nesse exemplo não é seguro, porém, oferece uma demonstração
básica de como esses programas funcionam.

PASSO 1: DESIGN DO PROGRAMA E ESTRUTURAS DE DADOS

Queremos executar esse programa com um argumento de linha de comando correspondente ao nome da conta – por
exemplo, e-mail ou blog.
A senha dessa conta será copiada para o clipboard para que o usuário possa colá-la num campo de Senha.
Dessa maneira, o usuário poderá ter senhas longas e complexas sem a necessidade de memorizá-las.
Abra uma nova janela no editor de arquivo e salve o programa como pw.py.
O programa deve começar com uma linha contendo #! (shebang), e você também deve escrever um comentário que
descreva brevemente o programa.
Como queremos associar o nome de cada conta à sua senha, podemos armazenar essas informações como strings
num dicionário.
O dicionário será a estrutura de dados que organizará os dados das contas e senhas.

PASSO 2: TRATAR ARGUMENTOS DA LINHA DE COMANDO

Os argumentos da linha de comando serão armazenados na variável sys.argv.
O primeiro item da lista sys.argv sempre será uma string contendo o nome do arquivo do programa ('pw.py'),
e o segundo item deverá ser o primeiro argumento da linha de comando.
Nesse programa, esse argumento será o nome da conta cuja senha você deseja obter.
Como o argumento de linha de comando é obrigatório, você deve exibir uma mensagem de uso ao usuário caso
ele se esqueça de adicioná-lo.

PASSO 3: COPIAR A SENHA CORRETA

Agora que o nome da conta está armazenado como uma string na variável account, devemos verificar se ele
existe no dicionário SENHAS como uma chave.
Em caso afirmativo, devemos copiar o valor da chave para o clipboard usando pyperclip.copy().
Observe que não precisamos realmente da variável account; poderíamos simplesmente usar sys.argv[1] em
todos os lugares em que account é usado nesse programa.
Porém, uma variável chamada account é muito mais legível do que algo enigmático como sys.argv[1].

Esse novo código procura o nome da conta no dicionário SENHAS.
Se o nome da conta for uma chave no dicionário, leremos o valor correspondente a essa chave, copiaremos
esse valor para o clipboard e exibiremos uma mensagem informando que o valor foi copiado.
Caso contrário, exibiremos uma mensagem informando que não há nenhuma conta com esse nome.
Esse é o script completo.
Será necessário modificar o valor do dicionário SENHAS no código-fonte sempre que você quiser atualizar
o programa com uma nova senha.
É claro que, provavelmente, você não vai querer manter todas as suas senhas num local em que qualquer
pessoa poderia copiá-las facilmente.
No entanto, esse programa poderá ser modificado e usado para copiar textos normais rapidamente para o
clipboard.
Suponha que você esteja enviando diversos e-mails, com muitos dos mesmos parágrafos em comum.
Você poderia colocar cada parágrafo como um valor no dicionário SENHAS (é provável que você queira
renomear o dicionário a essa altura); desse modo, você terá uma maneira de selecionar e copiar
rapidamente uma das várias partes de texto padrão para o clipboard.
No Windows, um arquivo batch poderá ser criado para executar esse programa com a janela Run de WIN-R.
Digite o seguinte no editor de arquivo e salve como
    1 - salvar pw.bat na pasta C:\Windows:
    2 - no prompt: cd c:\Windows
    3 - CTRL+C, CTRL+V: @py.exe C:\Users\Daniel\Downloads\Python\Projetos\pw.py <nome_da_conta>
Com esse arquivo batch criado, executar o programa de senhas protegidas no Windows é somente uma questão
de pressionar WIN-R e digitar pw <nome da conta>.
"""


# ! python 3


import sys
import pyperclip as ppc


dicionario_senhas = {
    'e-mail': '#S%k23',
    'blog': 'KOWB90$#ddd',
    'xp_invest': 'ZANP4023$h',
    'windows_xp': 'landie_342@K@',
    'academia': 'maromba23$23@'
}


conta = sys.argv[1]       # por default, sys.argv[0] é o nome do módulo / sys.argv[1] chamará a chave do dicionário

if conta in dicionario_senhas:
    ppc.copy(dicionario_senhas[conta])        # copia para o clipboard a senha da conta
    print(f'A senha da conta: {conta} foi copiada com sucesso!')
else:
    print('Conta incorreta ou inexistente.')

