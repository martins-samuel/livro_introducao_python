'''Faça um programa que peça dois números inteiros. 
Imprima a soma desses dois números na tela.''' 
while True:
    try:
        n1 = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('O primeiro número não é inteiro. Digite outro número que seja inteiro')
while True:
    try: 
        n2 = int(input('Digite o outro número inteiro: '))
        break
    except ValueError:
        print('O segundo número não é inteiro. Digite outro número que seja inteiro ')
soma = n1 + n2 
print(f'A soma é {soma}')