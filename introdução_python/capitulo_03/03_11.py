'''Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.'''
while True:
    try:
        preco = float(input('Digite o preço do produto: ').replace(',','.'))
        if preco < 0:
           raise ValueError ('Digite um preço positivo')
        break
    except ValueError as e:
        print(f'Error: {e}.Tente novamente')
while True:
    try:
        desconto = float(input('Digite a porcentagem de desconto: ').replace(',','.'))
        if desconto < 0:
            raise ValueError ('Digite um valor positivo')
        break
    except ValueError as e:
        print(f'Error: {e}.Tente novamente')
preco_com_desconto = preco * (1-(desconto/100))
print(f'O seu produto com desconto fica {preco_com_desconto:.2f}')