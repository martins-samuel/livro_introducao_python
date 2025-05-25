'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1,250, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.'''
while True:
    try:
        salario = float(input('Digite o valor do seu salário: ').replace(',','.'))
        if salario <= 0:
            print('Informe um salário positivo.')
        else:
            break
    except ValueError:
        print('Valor errado.Informe outro por favor!')
if salario > 1250:
    aumento = salario * 1.1 
    print(f'Seu novo salário com um aumento de 10% é {aumento}')
else:
    aumento = salario * 1.15
    print(f'O seu novo salário com aumento de 15% é {aumento}')