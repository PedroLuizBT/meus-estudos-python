nome = str(input('Qual o seu nome?'))
turma = str(input('Qual a sua turma?'))
materia = str(input('qual a matéria? '))
nota1 = float(input('Qual o valor da sua primeira nota? '))
nota2 = float(input('Qual o valor da sua segunda nota? '))

media = (nota1 + nota2) / 2

print(f'Olá {nome} da turma {turma}, sua média na matéria {materia} foi de {media}')