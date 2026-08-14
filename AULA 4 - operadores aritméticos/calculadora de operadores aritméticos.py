#Ordem de precedência dos operadores aritméticos
#1 () qualquer número entre parênteses é calculado primeiro
#2 ** exponenciação
#3 * / // % multiplicação, divisão, divisão inteira e resto da divisão
#4 + - adição e subtração

print('------calculadora de operadores aritméticos------')

n1 = int(input('Digite um número pra somar: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2

n3 = int(input('Digite um número para subtrair: '))
n4 = int(input('Digite outro número: '))
subtracao = n3 - n4

n5 = int(input('Digite um número para multiplicar: '))
n6 = int(input('Digite outro número: '))
multiplicacao = n5 * n6

n7 = int(input('Digite um número para dividir: '))
n8 = int(input('Digite outro número: '))
divisao = n7 / n8  

n9 = int(input('Digite um número para calcular a elevação: '))
n10 = int(input('Digite o expoente: '))
elevacao = n9 ** n10

n11 = int(input('Digite um número para calcular a raiz quadrada: '))
raiz_quadrada = n11 ** (1/2)

n12 = int(input('Digite um número para calcular a divisão inteira: '))
n13 = int(input('Digite outro número: '))
divisao_inteira = n12 // n13

n14 = int(input('Digite um número para calcular o resto da divisão: '))
n15 = int(input('Digite outro número: '))
resto_divisao = n14 % n15   

print('------calculadora de operadores aritméticos------')
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Elevação: {elevacao}')
print(f'Raiz Quadrada: {raiz_quadrada}')
print(f'Divisão Inteira: {divisao_inteira}')
print(f'Resto da Divisão: {resto_divisao}')