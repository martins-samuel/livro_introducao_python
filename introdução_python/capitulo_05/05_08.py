'''Escreva um programa que leia dois números. 
Imprima o resultado da multiplicação do primeiro pelo segundo. 
Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender a multiplicação de dois números 
como somas sucessivas de um deles. Assim,4x5=5+5+5+5=4+4+4+4+4.'''
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print('1- Deseja calcular a multiplicação de dois números')
    print('2- Encerrar o programa')
    try: 
        opcao = int(input('Digite a sua opcão escolhida: '))
        match opcao:
            case 1:
                n1 = int(input('Digite o primeiro número a ser multiplicado: '))
                n2 = int(input('Digite o segundo número a ser multiplicado: ')) 
                resultado = 0
                contador = 0
                while contador < abs(n2):
                    resultado += n1
                    contador += 1
                    
                 # Corrige o sinal, se n2 for negativo
                if n2 < 0:
                    resultado = -resultado
                print(f'{n1} x {n2} = {resultado}')
            case 2:
                limpar()
                print('Programa encerrado com sucesso')
                
                break   
            case _:
                limpar()
                print('Digite uma entrada válida. Números do tipo inteiro')
    except Exception as e:
        print(f'Digite um valor válido. {e}')