'''Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.'''
while True:
    try:
        km = float(input('Digite os km que você já percorreu:').replace(',','.'))
        if km <= 0:
            print('A distância a percorrida tem que ser maior que zero.Tente novamente!')
            continue
        break
    except ValueError as e:
        print(f'Digite os km percorrido do tipo real')
if km <= 200:
    viagem_preco = km * 0.5
else:
    viagem_preco = km * 0.45 
print(f'O valor da sua viagem ficou R$: {viagem_preco:.2f}')
    
        