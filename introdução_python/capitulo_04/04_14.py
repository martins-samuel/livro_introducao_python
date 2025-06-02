'''Reescreva o programa a seguir com if-elif-else. 
Adicione as linhas necessárias para fazê-lo funcionar em Python.
if a < 10;
    print("a é menor que 10") 
if a >= 10 and a < 20: 
    print("a é maior que 10 e menor que 20") 
if a >= 20:
    print("a é maior que 20")'''
while True:
    try:
        a = float(input('Digite um número real que seja positivo ').replace(',','.'))
        if a > 0:
            print('Carregando.....')
            break
        else:
            print('Valor inválido')
            continue   
    except ValueError:
        print('Digite um valor válido    ')
if a < 10:
    print(f'A é menor que 10 {a}')
elif a >= 10 and a < 20:
    print(f' O valor de a {a} é > que 10 é < menor que 20')
else:
    print(f'A é maior que vinte')