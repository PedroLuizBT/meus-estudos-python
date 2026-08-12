nome = str(input('Qual o seu nome?'))
idade = int(input('Qual a sua idade?'))
altura = float(input('Qual a sua altura?'))
maior_idade = idade >= 18

print('O seu nome é:', nome,type(nome))
print('A sua idade é:', idade,type(idade))
print('A sua altura é:', altura,type(altura))
print('Você é maior de idade?', maior_idade,type(maior_idade))