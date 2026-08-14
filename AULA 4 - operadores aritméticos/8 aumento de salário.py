nome = str(input('Qual o seu nome, funcionário pagão? '))
salario = float(input('Qual o seu salário atual? '))

aumento = salario + (salario * 0.15)

print(f'Parabéns {nome} seu bobão, antes o seu salário era de R${salario:.2f}, e agora com o aumento da promoção, você receberá R${aumento:.2f}')
