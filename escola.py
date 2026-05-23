nome = input('digite seu nome')
idade = int(input('digite sua idade')) 

if idade >= 18:
    print('voce é maior de idade')

    cnh = input('voce possui cnh? (sim/não):')
    if cnh.lower() == 'sim':
       print('parabens,voce pode dirigir')
    else:
        print("voce nao pode dirigir")   
else:
     print(f'{nome}, vove é menor de idade.')



