nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("voçe esta a baixo do peso")



else:
    print("voçe esta acima do peso")




