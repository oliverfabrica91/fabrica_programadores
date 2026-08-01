#autor: oliver da silva santos
#projeto entendendo tratamento de exceções

try:
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))

    # Calcular o IMC
    def calcular(peso, altura):
        imc = peso / (altura ** 2)
        print(f'Seu IMC é: {imc:.2f}')

    calcular(peso, altura)

except:
    print('Erro: digite apenas números')










