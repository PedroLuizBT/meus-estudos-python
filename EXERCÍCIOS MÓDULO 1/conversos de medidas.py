metro = float(input('Escreva uma distância em metros: '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro / 0.1
cm = metro / 0.01
mm = metro / 0.001

print('---------------------conversor de medida de metro---------------------')
print(f'A medida de {metro}m corresponde a: \n{km}km \n{hm}hm \n{dam}dam \n{dm}dm \n{cm}cm \n{mm}mm')