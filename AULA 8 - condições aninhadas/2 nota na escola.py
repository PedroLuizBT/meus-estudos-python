nota_1 = float(input('Qual a nota da sua primeira prova? '))
nota_2 = float(input('Qual a nota da sua segunda prova? '))

media = (nota_1 + nota_2) / 2

if media >= 10:
    print('Você tirou a nota MÁXIMA, parabéns!!')

elif media >= 8:
    print('Sua nota foi muito boa!')

elif media >= 7:
    print('Passou na prova, mas poderia ser melhor... Mas tá bom também')

elif media >= 5:
    print('Foi por pouco, estude mais na próxima vez')

elif media >= 3:
    print('Nem tentou né seu safado! ESTUDE SEU BEM MAIS SEU BOBÃO')

else:
    print('O Zero meia você é um DEMÔNIO, ESTUDE DIREITO SEU CATIÇO')