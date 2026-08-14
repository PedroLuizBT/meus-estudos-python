

nome = str(input('Qual o seu nome?'))
cpf = str(input('Qual o seu CPF?'))
qtd_produto = int(input('Quantos produtos deseja comprar?'))
valor_total = float(input('Qual o valor total da compra? R$'))
cartao_fidelidade = str(input('Você possui o cartão fidelidade? Sim/não:'))

valor_alto = valor_total >= 200
tem_cartao = cartao_fidelidade == 'sim'

print('Nome do cliente:', nome, type(nome))
print('CPF do cliente:', cpf, type(cpf))
print('Quantidade de produtos comprados:', qtd_produto, type(qtd_produto))
print('Valor total da compra: R$', valor_total, type(valor_total))
print('Possui cartão fidelidade:', cartao_fidelidade, type(cartao_fidelidade))
print('Valor é alto?', valor_alto, type(valor_alto))
print('Tem cartão fidelidade (bool)?', tem_cartao, type(tem_cartao))
