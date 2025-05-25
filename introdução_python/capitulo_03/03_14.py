'''Escreva um programa que pergunte a quantidade de km percorridos 
por um carro alugado pelo usuário, assim como a quantidade de dias pelos 
quais o carro foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
while True:
    try:
        km = float(input('Digite a quaintade de KMs percorrido com o carro: ').replace(',','.'))
        if km <= 0:
            raise ValueError('Digite um valor maior que zero')
        break
    except ValueError as e:
        print('Digite um valor positivo e decimal')
while True:
    try:
        dia = int(input('Digite a quantidade de dias que o carro ficou alugado: ').replace(',','.'))
        if dia <= 0:
            raise ValueError('Digite um valor maior que zero')
        break 
    except ValueError as e:
        print('Digite um  valor positivo e inteiro')
total_pagar = (60 * dia) + (km * 0.15)
print(f'O valor em reias do aluguel ficou: {total_pagar:.2f}')