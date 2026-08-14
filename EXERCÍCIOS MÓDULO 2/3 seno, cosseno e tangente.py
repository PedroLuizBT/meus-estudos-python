import math
angulo = float(input('Digite o valor de um ângulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'Seno: {sen:.2f}')
print(f'cosseno: {cos:.2f}')
print(f'tangente: {tan:.2f}')
