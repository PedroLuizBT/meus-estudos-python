print('--------Questionário do velocímetro--------')
print('Olá senhor policial, tudo bem!')
modelo = str(input('Qual o modelo do carro do meliante? '))
placa = str(input('Qual a placa do carro do safado? '))
velocidade = int(input('Qual a velocidade que o maluco tava? '))

print('-------Conclusão do velocímetro-------')
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    print(f'O carro de modelo {modelo} e placa {placa} estava há {velocidade:.0f}Km/h')
    print(f'Logo o safado estava acima do limite de velocidade e deve ser multado em {multa:.2f}R$')
else:
    print(f'O carro de modelo {modelo} e placa {placa} estava há {velocidade:.0f}Km/h')
    print('Logo o parceiro estava abaixo do limite de velocidade e não deve ser multado')