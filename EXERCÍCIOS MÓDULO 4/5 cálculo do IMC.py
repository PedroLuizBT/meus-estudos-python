altura = float(input('Digite sua altura: '))

peso = float(input('Digite seu peso: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está abaixo do peso')

elif 18.5 <= imc <= 24.9:
    print('Você está saudável (peso normal)')

elif 25 <= imc <= 29.9:
    print('Você está sobrepeso')

elif 30 <= imc <= 34.9:
    print('Você está com obesidade grau 1')

elif 35 <= imc <= 39.9:
    print('Você está com obesidade grau 2')

else:
    print('Você está com obesidade grau 3(Mórbida)')