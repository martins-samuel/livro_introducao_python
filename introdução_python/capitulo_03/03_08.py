#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
while True:
    try:
        metro = float(input('Digite um valor em metros que seria convertido em milímetros: ').replace(',','.'))
        break
    except ValueError:
        print('Digite um valor de entrada do tipo real.')
milimetro = metro * 1000
print(f'O valor convertido para milimetros é {milimetro:.2f}')
    
