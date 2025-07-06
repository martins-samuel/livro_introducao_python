'''Escreva um programa que leia dois números. 
Imprima a divisão inteira do primeiro pelo segundo, 
assim como o resto da divisão. 
Utilize apenas os operadores de soma e 
subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da 
divisão de dois números como a quantidade de vezes 
que podemos retirar o divisor do dividendo. 
Logo, 20 + 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.

'''
import os
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print('1- Desejar dividir dois números')
    print('2- Encerrar o programa')
    try:
        opcao = float(input('Digite a seu opção escolhida: ').replace(',','.'))
        match opcao:
            case 1:
                n1 = float(input('Digite o número que você deseja dividir: ').replace(',', '.'))
                n2 = float(input('Digite pelo o que você quer dividir: ').replace(',', '.'))

                if n2 == 0:
                    print('Não existe divisão por zero.')
                    continue

                resultado = 0
                contador = 0

                negativo = False
                if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
                    negativo = True

                # Converte para inteiros para aplicar divisão inteira com resto
                dividendo = abs(int(n1))
                divisor = abs(int(n2))

                while dividendo >= divisor:
                    dividendo -= divisor
                    resultado += 1

                if negativo:
                    resultado = -resultado

                resto = dividendo

                print(f'{int(n1)} / {int(n2)} = {resultado} com resto {resto}')
            case 2:
                limpar()
                print('Programa encerrado! ')
                break 
                
            case _: 
                limpar()
                print('Entrada inválida digite uma opção válida')
                continue
                
    
    except Exception as e:
        print('Digite um valor valor do tipo float')