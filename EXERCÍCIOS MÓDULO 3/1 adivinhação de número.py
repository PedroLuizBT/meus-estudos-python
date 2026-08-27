import random

numero1 = random.randint(1, 5)
adivinhacao = int(input('Tente adivinhar um número de 1 a 5: '))

print(f'O número sorteado foi {numero1}')
if adivinhacao == numero1:
    print('Você deve ser o Patrick Jane')
else:
    print('Você errou, deve ser a Lisbon')
