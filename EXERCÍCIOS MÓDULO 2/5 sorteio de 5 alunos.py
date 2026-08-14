import random

nome1 = 'Pedro Luiz'
nome2 = 'Maria Julia'
nome3 = 'Laurinha Pessurno'
nome4 = 'Davi Romagnoli'
nome5 = 'Sofia Livino'

alunos = [nome1, nome2, nome3, nome4, nome5]
random.shuffle(alunos)

print("Ordem de apresentação do trabalho após o sorteio foi:")
print(alunos[0])
print(alunos[1])
print(alunos[2])
print(alunos[3])
print(alunos[4])