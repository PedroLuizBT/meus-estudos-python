import math
hipotenusa = float(input('Digite o comprimento da hipotenusa: '))
cateto_1 = float(input('Dgitie o comprimento de um cateto '))
cateto_2 = math.sqrt(hipotenusa**2 - cateto_1**2)

print(f"O comprimentp de outro cateto é: {cateto_2:.2f}")