#autor: oliver da silva santos
#projeto entendendo tratamento de exceções



try:
    altura = float(input("Digite a altura: "))
    peso = float(input("Digite o peso: "))
    imc =  peso /(altura **2)
    print(f"o resultado da imc é: {imc:.2f}")
except:
    print("digite apenas números.") 







    