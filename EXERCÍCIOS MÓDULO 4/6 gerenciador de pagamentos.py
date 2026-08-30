produto = str(input('Digite o produto que você quer comprar: '))
preco = float(input('Digite o preço do produto: '))
forma_pagamento = str(input('Digite a forma de pagamento: '))

if forma_pagamento == 'a vista no dinheiro':
    vista_dinheiro = preco * 0.9
    print(f'O produto {produto} vai custar {vista_dinheiro}')

elif forma_pagamento == 'a vista no cartão':
    vista_cartao = preco * 0.95
    print(f'O produto {produto} vai custar {vista_cartao}')

elif forma_pagamento == 'cartão 2x':
    cartao_2x = preco
    print(f'O produto {produto} vai custar {cartao_2x}')

elif forma_pagamento == 'cartao 3x':
    tempo_parcela = int(input('Digite em quantas vezes quer parcelar a compra: '))
    cartao_3x_mais = preco * tempo_parcela * 1.2
    print(f'O produto {produto} vai custar {cartao_3x_mais}')
    
else:
    print('Forma de pagamento inválida')