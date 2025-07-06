'''Modifique o programa anterior de forma que o usuário também 
digite o início e o fim da tabuada, em vez de começar com 1 e 10.'''
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print('1- Deseja ver a tabuada')
    print('2- Encerrar o programa')
    try:
        opcao = int(input('Qual opção escolhida: '))
        
        match opcao:
            case 1:
                try:
                    n = int(input('Digite a tabuada do número escolhido: '))
                    inicio = int(input('Digite o primeiro número da tabuada: '))
                    fim = int(input('Digite o último número da tabuada: '))
                    if inicio >= fim:
                        print('O valor de início tem que ser menor que o valor do fim da tabuada') 
                        limpar()
                        continue
                       
                    while inicio <= fim:
                        print(f'{n} X {inicio} = {n * inicio}')
                        inicio += 1
                except ValueError:
                    print('Digite um número inteiro válido!')  
            case 2:
                print('Programa encerrado!')
                break
            case _:
                print('Entrada inválida')  
    except ValueError:
        print('Digite apenas números inteiros!')                