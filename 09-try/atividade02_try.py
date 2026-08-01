#autor: oliver da silva santos
#projeto entendendo tratamento de exceções

try:
    celsius = float(input("Digite o valor em Celsius: "))
    graus = (celsius * (9/5)) + 32
    print(f"o resultado da conversão em fahrenheit: {graus:.2f}")
except:
    print("digite apenas numeros.")
    
