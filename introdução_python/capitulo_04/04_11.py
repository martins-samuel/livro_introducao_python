'''Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário.
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.'''
while True:
    try:
        casa = float(input('Digite o valor da casa que voce gostaria de financiar R$: ').replace(',','.'))
        if casa <= 0:
            print('O valor da casa deve ser positivo. Por favor, tente novamente.')
            continue
        break
    except ValueError:
        print('Entrada inválida para o valor da casa. Digite apenas números positivos.')
while True:
    try:
        salario = float(input('Digite o valor do seu salário R$ : ').replace(',','.'))
        if salario <= 0:
            print('O salário deve ser positivo. Por favor, tente novamente.')
            continue
        break
    except ValueError:
        print('Entrada inválida!')
while True:
    try:
        anos = int(input('Digite a quatindade de anos que gostaria de financiar: '))
        if anos <=0:
            print('O número de anos deve ser positivo. Por favor, tente novamente.')
            continue
        break
    except ValueError as e:
        print(f'Digite um valor válido {e}')
prestacao = casa/(anos * 12)
condicao_salario = salario * (30/100)
if prestacao >= condicao_salario:
    print('Infelizmente não é possível aprovar o empréstimo')
else:
    print('Empréstimo aprovado ')