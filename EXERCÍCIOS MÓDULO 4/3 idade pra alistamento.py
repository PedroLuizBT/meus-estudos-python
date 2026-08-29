ano = 2026
ano_nasc = int(input('Digite abaixo em que ano você nasceu\nAno de nascimento: '))
idade = ano - ano_nasc
tempo_faltante = 18 - idade
tempo_passado = idade - 18

if idade == 17:
    print('Você deve se alistar daqui a 1 ano ')
elif idade <= 16:
    print(f'Você deve se alistar daqui a {tempo_faltante} anos')
elif idade == 19:
    print('Você devia ter se alistato há 1 ano')
elif idade >= 20:
    print(f'Você devia ter se alistado há {tempo_passado} anos! Vai cumprir punição jumento')
else:
    print('Está na hora de você se alistar!')