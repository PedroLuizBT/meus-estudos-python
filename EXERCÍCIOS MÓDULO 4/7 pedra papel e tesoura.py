import random

opcoes = ['pedra', 'papel', 'tesoura']
computador = random.choice(opcoes)

sua_escolha = str(input('Escolha pedra, papel ou tesoura: '))

if sua_escolha == computador:
    print(f'Empate!\nVocê escolheu {sua_escolha} e o computador escolheu {computador}')
elif sua_escolha == 'pedra' and computador == 'tesoura':
    print(f'Você venceu!\nVocê escolheu {sua_escolha} e o computador escolheu {computador}')
elif sua_escolha == 'papel' and computador == 'pedra':
    print(f'Você venceu!\nVocê escolheu {sua_escolha} e o computador escolheu {computador}')
elif sua_escolha == 'tesoura' and computador == 'papel':
    print(f'Você venceu!\nVocê escolheu {sua_escolha} e o computador escolheu {computador}')
else:
    print(f'Você perdeu!\nVocê escolheu {sua_escolha} e o computador escolheu {computador}')