ano = 2026
ano_nasc = int(input('Digite abaixo o ano em que você nasceu\nAno de nascimento: '))
idade = ano - ano_nasc

if idade <= 9:
    print('Você é um nadador mirim')
elif 14 >= idade > 9:
    print('Você é um nadador infantil')
elif 19 >= idade > 14:
    print('Você é um nadador junior')
elif 25 >= idade > 19:
    print('Você é um nadador sênior')
else:
    print('Você é um nadador master')