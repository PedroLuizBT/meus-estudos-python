altura = float(input('Qual a altura da sua parede em metros? '))
largura = float(input('Qual a largura da sua parede em metros? '))

litro = (altura * largura) / 2

print(f'Para pintar uma parede de {altura} metros de altura e {largura} metros de largura, você precisará de {litro:.2f} litros de tinta')
