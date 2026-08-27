nota1 = float(input('Digite a nota da sua primeira prova: '))
nota2 = float(input('Digite a nota da sua segunda prova: '))
media = (nota1 + nota2) / 2

print(f'Sua média foi {media:.1f}')
if media >= 6:
    print('Você foi aprovado, parabéns garanhão!!')
else:
    print('Você foi reprovado seu bundâo, estuda mais na próxima!!')