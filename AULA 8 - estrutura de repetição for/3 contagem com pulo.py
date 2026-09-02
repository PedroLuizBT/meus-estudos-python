inicio = int(input('Em que número você começa a andar? '))
fim = int(input('Em que número você termina de andar? '))
passada = int(input('Quantos números você pula por passada? '))

print(f'Você começa no {inicio}, termina no {fim} e pisa nos números:', end=' ')

for caminhada in range(inicio, fim, passada):
    print(caminhada, end=' ')

print()