'''Escreva um programa que pergunte a velocidade do carro de um usuário. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.
'''
while True:
    try:
        velocidade = float(input('Digite a sua velocidade em KM/H: ').replace(',','.'))
        if velocidade <= 0:
            print('Digite um velocidade do tipo positiva')
        else:
            break
    except ValueError as e:
        print(f'Error: {e}')
if velocidade > 80:
    multa = (-80 + velocidade) * 5
    print(f'O valor da sua multa é R$: {multa:.2f}') 
else:
    print('Você está dentro do limite de velocidade. Boa viagem')
