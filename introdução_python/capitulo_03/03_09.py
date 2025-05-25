#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
while True:
    try:
        dia = int(input('Digite a quantidade de dias que deseja transformar em segundos: '))
        hora = int(input('Digite a quantidade de horas que deseja transformar em segundos: '))
        minuto = int(input('Digite a quantidade de minutos que deseja transformar em segundos: '))
        segundo = int(input('Digite a quantidade de segundos: '))
        break
    except ValueError:
        print('Digite um valor do tipo inteiro')
dia_para_segundos = dia * 24 * 60 * 60 
hora_para_segundos = hora * 60 * 60 
minuto_para_segundos = minuto * 60 
soma_de_todos_segundos = dia_para_segundos + hora_para_segundos + minuto_para_segundos + segundo
print(f'Tudo transformado em segundos fica {soma_de_todos_segundos}')