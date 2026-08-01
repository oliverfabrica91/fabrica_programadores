# autor: oliver da silva santos
# projeto entendendo tratamento de exceções

try:
    reais = float(input("Digite o valor em real: "))
    cotacao = float(input("Digite o valor em dolar: "))
    dolares = reais / cotacao
    print(f"o resultado da conversão é: {dolares:.2f}")
except:
    print("digite apenas numeros.")
        