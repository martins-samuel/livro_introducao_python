'''Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências,
I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
''' """
+-----------------------------------------------------+
|         Preço por tipo e faixa de consumo           |
+-----------------------------------------------------+
| Tipo        | Faixa (kWh)      | Preço            |
+-----------------------------------------------------+
| Residencial | Até 500          | R$ 0,40          |
|             | Acima de 500     | R$ 0,65          |
+-----------------------------------------------------+
| Comercial   | Até 1000         | R$ 0,55          |
|             | Acima de 1000    | R$ 0,60          |
+-----------------------------------------------------+
| Industrial  | Até 5000         | R$ 0,55          |
|             | Acima de 5000    | R$ 0,60          |
+-----------------------------------------------------+
"""
while True:
    try:
        kwh = float(input('Digite a quantidade de Kwh consumido nesse mês: ').replace(',','.'))
        if kwh <=0:
            print('Digite uma entrada positiva.')
        else:
            break # Sai se for feita umma entrada válida
    except ValueError:
        print('Digite uma entrada válida!')
        continue  
while True:
    try:
        print('R = residências\n I = indústria\n C = comércio\n')
        print('Qual é o tipo da sua instalação? ')
        tipo_instalacao = (input('Minha instalação é: ')).upper().strip()
        if tipo_instalacao in ['R', 'I', 'C']:
            break # Sai do loop se a entrada for válida
        else:
            print('Hmm, essa opção não existe. Por favor, digite R, I ou C.')
    except ValueError:
        print('Digite uma entrada válida')
        continue
if tipo_instalacao == 'R':
    if kwh < 500:
        conta_pagar = kwh * 0.4
    else:
        conta_pagar = kwh * 0.65
if tipo_instalacao == 'C':
    if kwh < 1000:
        conta_pagar = kwh * 0.55
    else:
        conta_pagar = kwh * 0.6
if tipo_instalacao == 'I':
    if kwh < 5000:
        conta_pagar = kwh * 0.55
    else:
        conta_pagar = kwh * 0.6
print(f'A sua conta deu em R$: {conta_pagar} e  kwh consumido nesse mês foi {kwh}')