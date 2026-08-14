import math #importanto a biblioteca de matemática 'math'

n1 = int(input('Digite um número: '))

raiz = math.sqrt(n1) #math.sqrt é uma função da biblioteca 'math' que realiza a raiz quadrada, logo raiz quadrada = math.sqrt

print(f'A raíz de {n1} arredondada pra cima é igual a {raiz}')
print(f'A raíz de {n1} arredondada pra cima é igual a {math.ceil(raiz)}') #math.ceil serve pra arredondar pra cima
print(f'A raíz de {n1} arredondada pra baixo é igual a {math.ceil(raiz)}') #math.floor serve pra arredondar pra pra baixo