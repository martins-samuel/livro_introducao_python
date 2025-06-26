'''Corrija o programa a seguir: 
média = input("Digite sua média:") 
if média < 4: 
    print("Infelizmente você reprovou") 
if média < 7: 
    print("Você ficou de recuperação") 
if média > 7: 
    print("Você passou de ano")'''
while True:
    try:
        media = float(input('Digite a sua média no ano letivo: ').replace(',','.'))
        if media > 0:
            break
        else:
            print('Digite um valor positivo de média') 
    except ValueError:
        print("Digite um valor do tipo real positivo !")
if media < 4:
    print('Infelizmente você reprovou !')
elif media < 7:
    print('Você ficou de recuperação ')
else:
    print('Você passou de ano ')    