salario = float(input('Digite seu salário mensal: '))
valor_casa = float(input('Digite o valor da casa que você quer financiar: '))
anos_pagar = int(input('Digite em quantos anos você vai pagar a casa: '))
mensalidade = (valor_casa / anos_pagar) / 12

if mensalidade <= salario * 0.30:
    print('O financiamento pode ser realizado.')
    print(f'O valor da mensalidade é {mensalidade:.2f}R$')
else: 
    print('Empréstimo negado')
    print('Mensalidade muito alta para seu salário')