'''Escreva um programa para calcular a redução do tempo de vida de um fumante. 
Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
Considere que um fumante perde 10 minutos de vida a cada cigarro, 
e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.'''
while True:
    try:
        cigarros_por_dia = int(input('Digite a quantidade de cigarros fumados por dia: '))
        if cigarros_por_dia <= 0:
            raise ValueError('Digite um valor maior que zero')
        break
    except ValueError as e:
        print(f'Erro: {e}. Digite um número inteiro e positivo.')

while True:
    try:
        anos_fumando = float(input('Digite há quantos anos você fuma: ').replace(',', '.'))
        if anos_fumando <= 0:
            raise ValueError('Digite um valor maior que zero')
        break
    except ValueError as e:
        print(f'Erro: {e}. Digite um número positivo e real.')


total_cigarros = cigarros_por_dia * 365 * anos_fumando
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / (60 * 24)

print('-' * 50)
print(f'O total estimado de dias de vida perdidos é: {dias_perdidos:.2f} dias.')
print('Programa encerrado.')
print('-' * 50)
