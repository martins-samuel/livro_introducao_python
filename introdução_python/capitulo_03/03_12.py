'''Escreva um programa que calcule o tempo de uma viagem de carro; 
Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
'''
while True:
    try:
        distancia = float(input('Digite a distância em KM a ser percorrida no trajeto da viagem: ').replace(',','.'))
        if distancia <= 0:
            raise ValueError ('Digite um valor positivo') 
        break
    except ValueError as e :
        print(f'Error: {e}.Tente novamente')
while True:
    try:
        velocidade_media = float(input('Digite a velocidade média que você vai correr: ').replace(',','.'))
        if velocidade_media <= 0:
            raise ValueError('Digite um valor positivo') 
        break 
    except ValueError as e:
        print(f'Error: {e}. Tente novamente')    
tempo = distancia/velocidade_media 
print('-'*50)
print(f'O tempo médio da viagem vai ser de {tempo:.2f} horas')
print('Programa encerrado')
print('-'*50)