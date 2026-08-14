nome = str(input('Qual o seu nome?: '))
print('Olá, prazer em te conhecer, {:20}!'.format(nome)) #faz o total de caracteres ser 20, caso o nome tenha menos que 20, ele preenche com espaços em branco.

print('Olá, prazer em te conhecer, {:>20}!'.format(nome)) #faz a mesma coisa, mas o texto fica mais a direita

print('Olá, prazer em te conhecer, {:^20}!'.format(nome)) #faz a mesma coisa, mas o texto fica mais no centro

print('Olá, prazer em te conhecer, {:=^20}!'.format(nome)) #agora ele preenche os espaços com o caractere que vem antes do ^, nesse caso o =.