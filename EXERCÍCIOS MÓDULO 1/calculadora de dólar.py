nome = str(input('Qual o seu nome? '))
dinheiro = float(input('Quantos reais você tem na carteira? '))

dolar = dinheiro / 5.22

print(f'Fala comigo {nome}, você tem R${dinheiro:.2f} na carteira, e convertendo em dólar, isso da Us${dolar:.2f} doláres.')