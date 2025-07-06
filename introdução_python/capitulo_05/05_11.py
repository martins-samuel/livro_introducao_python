'''Escreva um programa que pergunte o depósito inicial e à 
taxa de juros de uma poupança. Exiba os valores mês a mês 
para os 24 primeiros meses, Escreva o total ganho com juros no período.'''
deposito_inicial = float(input('Digite o seu depósito inicial R$: ').replace(',', '.'))
taxa_juros = float(input('Digite a taxa de juros (ex: 0.01 para 1%): ').replace(',', '.'))

saldo = deposito_inicial
total_juros = 0

for mes in range(1, 25):
    juros = saldo * taxa_juros
    saldo += juros
    total_juros += juros
    print(f'Mês {mes}: saldo = R$ {saldo:.2f}')

print(f'\nTotal ganho com juros em 24 meses: R$ {total_juros:.2f}')