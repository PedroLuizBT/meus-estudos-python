print('---ficha de inscrição de corrida---')
nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))
peso = float(input('Qual o seu peso em Kg? '))
tempo = float(input('Em quantos minutos pretende terminar a corrida? '))
ja_correu = str(input('Você já correu alguma vez? (sim/não) ')).strip().lower()

apto_idade = idade >= 16
experiente = ja_correu == 'sim'
meta_rapida = tempo <= 120

print('---ficha do corredor---')
print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Peso: {peso} Kg')
print(f'Tempo pretendido: {tempo} minutos')
print(f'É apto para a corrida: {apto_idade}',type(apto_idade))
print(f'É experiente: {experiente}',type(experiente))
print(f'Pretende terminar a corrida em menos de 120 minutos: {meta_rapida}',type(meta_rapida))