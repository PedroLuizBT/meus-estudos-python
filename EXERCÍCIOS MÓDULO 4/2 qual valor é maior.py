n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro número é maior que o segundo ({n1} > {n2})')
elif n1 < n2:
    print(f'O segundo número é maior que o primeiro ({n1} < {n2})')
else:
    print(f'Os números tem o mesmo valor ({n1} = {n2})')