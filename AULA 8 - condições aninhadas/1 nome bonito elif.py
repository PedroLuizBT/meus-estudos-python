nome = str(input('Qual é o seu nome? '))
if nome == 'Pedro':
    print('Que nome bonito meu chegado!!')
elif nome in ('Erik, Gustavo, Matheus'):
    print('Você é meu primo!')
elif nome == 'Malu':
    print('Você é minha prima!')
elif nome in ('Jorge, Tiago, Rodrigo'):
    print('Você é meu tio!')
elif nome in ('Renata, Meryellen'):
    print('Você é minha tia!')
elif nome == 'Glauce':
    print('Você é minha mãe!')
elif nome == 'Daniel':
    print('Você é meu pai!')
elif nome in ('Nádia, Socorro'):
    print('Você é minha avó!')
elif nome in ('Toninho, Barbosa'):
    print('Você é meu avô!')
else:
    print('Seu nome é meio sem sal, sla...')

print(f'Tenha um bom dia, {nome}!')