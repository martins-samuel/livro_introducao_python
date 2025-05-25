#Escreva um programa que leia três números e que imprima o maior e o menor.
while True:
    try:
        n1 = float(input('Digite o primeiro valor: ').replace(',','.'))
        n2 = float(input('Digite o segundo valor: ').replace(',','.'))
        n3 = float(input('Digite o terceiro valor: ').replace(',','.'))
        break
    except ValueError:
        print('Digite um valor do tipo real  ')
maior = n1 
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
menor = n1 
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(f'O maior número digitado é {maior}')
print(f'O menor número digitado é: {menor}')

