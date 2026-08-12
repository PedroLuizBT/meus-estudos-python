nome = str(input("Digite seu nome: "))
qtd_itens_carrinho = int(input("Digite a quantidade de itens no carrinho: "))
valor_do_item = float(input("Digite o valor do item: "))

total = valor_do_item * qtd_itens_carrinho
frete = total >= 100.00

print("O seu nome é:", nome, type(nome))
print("A quantidade de itens no carrinho é:", qtd_itens_carrinho, type(qtd_itens_carrinho))
print("O valor do item é:", valor_do_item, type(valor_do_item))
print("O total da compra é:", total, type(total))
print("Você tem frete grátis?", frete, type(frete))