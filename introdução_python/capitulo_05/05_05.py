#Reescreva o programa anterior para escrever os 10 primeiros múltíplos de 3. 
'''
fim = int(input("Digite o último número a imprimir:"))
x=0
while x <= fim: 
    print(x) 
    x = x + 2'''
print("Exibindo os 10 primeiros múltiplos de 3:")

multiplos_encontrados = 0 # Contador para saber quantos múltiplos já exibimos
numero_atual = 3          # Começamos com o primeiro múltiplo de 3

while multiplos_encontrados < 10: # O loop continua até encontrarmos 10 múltiplos
    print(numero_atual)         # Exibe o múltiplo atual
    numero_atual += 3           # Pula para o próximo múltiplo de 3 (3, 6, 9, ...)
    multiplos_encontrados += 1  # Incrementa o contador de múltiplos encontrados

print("Contagem concluída!")