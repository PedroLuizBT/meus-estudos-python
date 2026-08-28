km = float(input('Qual a distância em Quilômetros da sua viagem? '))

if km >= 200:
    preco = km * 1.50
else:
    preco = km * 1.45

print(f'A distância da viagem é de {km}Km e o preço da passagem é {preco:.2f}R$')