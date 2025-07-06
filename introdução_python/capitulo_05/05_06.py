'''Altere o programa anterior para exibir os resultados no 
mesmo formato de uma tabuada de multiplicação: 2x1 = 2, 2x2 = 4,...'''
# n = int(input("Tabuada de:")) x=1
# while x <= 10:
#     print(n + x)
#     X=X+1
while True:
    print('1 - Se deseja mais uma tabuada')
    print('2 - Encerrar o programa')  
    opcao = int(input('Digite a sua escolha: '))
    match opcao:  
        case 1:
            try:
                n = input('Tabuada de: ')
                n = int(n) #transformado a string no tipo int
                x = 1
                while x <= 10:
                    multiplicacao = n * x
                    print(f'{n} X {x} = {multiplicacao}')
                    x += 1 #incremento do valor a ser multiplicado
                    
            except Exception as e:
                print(f'Digite um valor inteiro! {e}')
        case 2:
            print('Programa encerrado! ')
            break
        case _:
            print('Opção inválida. Digite 1 ou 2.')
                    
           