'''Modifique o programa anterior para imprimir de 1 até o número 
digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
fim = int(input("Digite o último número a imprimir:"))
x=0
while x <= fim: 
    print(x) 
    x = x + 2'''
while True:
    try:
        fim = int(input("Digite o último número a imprimir:"))
        if fim > 0:
            break
        else:
            print('Entrada inválida ! Tem que ser inteiro maior que zero')
    except ValueError:
        print('Digite um valor válido do tipo inteiro maior que zero')
x = 1  
while x <= fim: 
    if x % 2 == 1:
        print(x) 
    x = x + 2
