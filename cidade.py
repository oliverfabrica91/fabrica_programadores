nome = input('digite seu nome')
telefone = input('me fale seu telefone')
cidade = input('me diga sua cidade')
salario = float(input('qual seu salario senhor'))

if salario >= 1000:
    print('voce tem uma quantia legal')
elif salario >=700:
    print('voce tem uma renda razoavel')
elif salario >=500:
    print('voce tem uma renda baixa')
else:
    print('sua renda é muito baixa') 
