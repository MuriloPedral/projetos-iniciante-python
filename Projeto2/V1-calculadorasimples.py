print('---Calculadora simples de dois números---')

op = input('Qual operação você gostaria de realizar? [A] adição, [S] subtração, [M] multiplicação e [D] divisão: ').upper().strip()
#Tem como você fazer assim também: op = op.upper()
#strip() tira os espaços no começo e no fim

n1 = int(input('Digite um primeiro número: '))
n2 = int(input('Digite um segundo número: '))

if op == 'A':
    a = n1 + n2
    print(a)
elif op == 'S':
    s = n1 - n2
    print(s)
elif op == 'M':
    m = n1 * n2
    print(m)
elif op == 'D':
    d = n1 / n2
    print(d)
