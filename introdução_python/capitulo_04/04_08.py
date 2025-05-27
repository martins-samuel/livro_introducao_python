'''Reescreva o Programa 44 e calcule a conta da operadora Tchau usando else.
# Programa 4.4: Cálculo da mensalidade de um plano de celular da operadora Tchau 
plano = input("Qual é o seu plano de celular? ") 
if plano == "falopouco":
    minutos no plano = 100
    extra = 0,20 
    preço = 50 
if plano == "falomuito":
    minutos no plano = 500 
    extra = 0,15 
    preço = 99 
if plano != "falopouco" and plano != "falomuito": 
    print("Não conheço este plano")
if plano == "falopouco" or plano == "falomuito”: 
    minutos consumidos = int(input("Quantos minutos você consumiu? ")) 
    print("Você vai pagar:") 
    print(f"Preço do plano R${preço:10.2f}") 
    suplemento = 0 
if minutos consumidos > minutos no plano: 
    suplemento = extra * (minutos consumidos - minutos no plano) 
    print(f"Suplemento R$(suplemento:10.2f)")
    print(f" Total R$(preço + suplemento: 10.2f)")'''
# Programa 4.4 (reescrito): Cálculo da mensalidade de um plano de celular da operadora Tchau
plano = input("Qual é o seu plano de celular? ")

if plano == "falopouco":
    minutos_no_plano = 100
    extra = 0.20
    preco = 50
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do plano R${preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print(f"Suplemento R${suplemento:10.2f}")
    print(f"Total R${preco + suplemento:10.2f}")
elif plano == "falomuito":
    minutos_no_plano = 500
    extra = 0.15
    preco = 99
    minutos_consumidos = int(input("Quantos minutos você consumiu? "))
    print("Você vai pagar:")
    print(f"Preço do plano R${preco:10.2f}")
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
        print(f"Suplemento R${suplemento:10.2f}")
    print(f"Total R${preco + suplemento:10.2f}")
else:
    print("Não conheço este plano")
    
        