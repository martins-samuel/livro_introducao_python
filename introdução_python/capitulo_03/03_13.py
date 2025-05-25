'''Escreva um programa que converta uma temperatura digitada em °C 
em °F A fórmula para essa conversão é: f = (9 * c)/5 +32'''
while True:
    try:
        c = float(input('Digite a temperatura em celsius que deseja converter para fahrenheit: ').replace(',','.'))
        break
    except ValueError as e:
        print(f'Digite um valor do tipo real {e} .Tente novamente')
f = (9 * c)/5 + 32
print(f'A temperatura transformada em fahrenheit fica: {f:.2f}°F')
