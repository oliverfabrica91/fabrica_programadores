# autor: oliver da silva santos
# projeto entendendo tratamento de exceções
try:
    valor1 = float(input("Digite O primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    soma = valor1 + valor2
    print(f"o resultado da soma é: {soma}")
except:
    print("digite apenas números.")
    