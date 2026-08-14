carro = str(input('Qual o modelo de carro que você alugou? '))
km = float(input('Quantos Km você rodou com ele? '))
dia = int(input('Quantos dias você esteve com ele alugado? '))

valor_km = km * 0.15
valor_dia = dia * 60
valor_total = valor_km * valor_dia

print(f'Se você usou o modelo "{carro}", andou {km}Km em {dia} dia/s, o valor total à pagar é R${valor_total:.2f}')