produto = str(input('Qual o produto que você quer comprar? '))
preco = float(input('Qual o preço do produto? '))

desconto = preco * 0.05
preco_final = preco - desconto

print(f'O produto {produto} que custava R${preco:.2f}, com desconto de 5% vai custar R${preco_final:.2f}.')