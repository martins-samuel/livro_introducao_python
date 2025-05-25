'''Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a porcentagem do aumento. 
Exiba o valor do aumento e do novo salário.'''
while True:
    try:
        salario = float(input('Digite o valor do seu salário atual para sabermos o aumento: ').replace(',','.'))
        if salario < 0:
            raise ValueError('O salário não pode ser negativo')
        break
    except ValueError as e:
        print(f'Erro: {e}. Faça denovo!')    
while True:    
    try:
        porcentagem = float(input('Digite a porcentagem do seu aumento: ').replace(',','.'))
        if porcentagem < 0:
            raise ValueError('O valor da porcentagem de aumento não pode ser negativo')
        break
    except ValueError as e:
        print(f'Erro: {e}. Faça denovo!')
salario_com_aumento = salario * (1+(porcentagem/100))
print(f'O seu novo salário é: {salario_com_aumento:.2f}')