'''Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
Exiba o resultado da operação solicitada,
'''

while True:
    try:
        print('Calculadora básica de python')
        print('-'*55)
        n1 = float(input('Digite o primeiro número: ').replace(',','.'))
        n2 = float(input('Digite o segundo número ').replace(',','.'))  
        print('-'*55)    
        print(' 0 - Sair do Programa\n 1 - SOMA\n 2 - SUBTRAÇÃO\n 3 - MULTIPLICAÇÃO\n 4 - DIVISÃO\n')  
        print('-'*55)
        operador = input('Selecione um operador: ')  
        match operador:
            case  "0" :
                print('Programa encerrado')
                break
            case  "1":
                print(f'{n1}+{n2}= {n1+n2:.2f} ')
                continue
            case  "2" :
                print(f'{n1}-{n2}= {n1-n2:.2f} ')
                continue
            case  "3":
                print(f'{n1}*{n2}= {n1*n2:.2f} ')
            case  "4":
                if n2 !=0:
                    print(f'{n1}/{n2} = {n1/n2:.2f}')
                    break
                else:
                    print('O denominador não pode ser negativo')
                    continue
    except ValueError:
        print('Digite um entrada válida como números do tipo REAL')
        
        
        '''while True:
    try:
        print('Calculadora básica de Python')
        print('-'*55)
        n1 = float(input('Digite o primeiro número: ').replace(',','.'))
        n2 = float(input('Digite o segundo número: ').replace(',','.'))
        print('-'*55)

        while True: # Novo loop para a seleção do operador
            print(' 0 - Sair do Programa\n 1 - SOMA\n 2 - SUBTRAÇÃO\n 3 - MULTIPLICAÇÃO\n 4 - DIVISÃO\n')
            print('-'*55)
            operador = input('Selecione um operador: ')

            match operador:
                case "0":
                    print('Programa encerrado. Até a próxima!')
                    exit() # Usa exit() para sair completamente do programa, pois estamos em um loop aninhado
                case "1":
                    print(f'{n1} + {n2} = {n1+n2:.2f}')
                    break # Sai do loop do operador e volta para o loop principal para novos números
                case "2":
                    print(f'{n1} - {n2} = {n1-n2:.2f}')
                    break
                case "3":
                    print(f'{n1} * {n2} = {n1*n2:.2f}')
                    break
                case "4":
                    if n2 != 0:
                        print(f'{n1} / {n2} = {n1/n2:.2f}')
                        break
                    else:
                        print('Erro: O denominador não pode ser zero. Tente novamente com outro denominador.')
                        # Não usa 'break' aqui, para que o loop do operador continue e o usuário possa tentar novamente
                case _: # Captura qualquer outra entrada inválida
                    print('Opção inválida. Por favor, selecione uma das opções de 0 a 4.')
            print('-'*55) # Adiciona uma linha para melhor legibilidade

    except ValueError:
        print('Entrada inválida! Por favor, digite números reais válidos (ex: 5 ou 2.5).')
        print('-'*55)
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}.')
        print('-'*55)'''