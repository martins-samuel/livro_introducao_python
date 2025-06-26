"""
Reescreva o programa a seguir com if-elif-else. 
hora = int(input("Digite a hora atual:")) 
if hora < 12: 
    print("Bom dia!") 
if hora >=12 and hora <=18: 
    print("Boa tarde!") 
if hora >=18: 
    print(“Boa noite!")
    """

while True:
    try:
       hora = int(input("Digite a hora atual (0-23): "))  
       if 0 <= hora <= 23:
           break # Se hora válida ele saiu do loop
       else:
           print('Hora inválida! Digite um horário entre 0h - 23h ') # continua o loop para pedir hora novamente
    except ValueError:
        print('Entrada inválida ! Por favor, digite um número inteiro para hora')  
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente! ")
if hora < 12:
    print('Bom dia !')
elif  hora <= 18:
    print('Boa tarde !')
else:
    print('Boa noite !')