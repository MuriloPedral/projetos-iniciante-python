print('---Conversor de Temperatura---')

escolha = input('[1] para converter de celsius para fahrenheit e [2] para fazer o inverso')
t = int(input('Qual é a temperatura?'))

if escolha == '1':
    F = t * 1.8 + 32
    print(F)
elif escolha == '2':
    C = (t - 32)/1.8
    print(C)
