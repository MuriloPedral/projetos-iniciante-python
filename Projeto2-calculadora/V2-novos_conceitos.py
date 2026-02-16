print('------------------------------')
print('         CALCULADORA')

historico = []

def somar():
    numero_passado = 0

    while True:
        try:
            numero = float(input('Digite um número: '))
            numero_passado += numero
            print(f'A soma atual é: {numero_passado}')

            continuar = input('Quer continuar somando? [s/n]: ').lower()
            if continuar == 'n':
                break
            elif continuar != 's':
                print('Entrada inválida, continuando soma...')
        except ValueError:
            print('Você digitou algo diferente de um número')

    historico.append('Soma:')
    historico.append(round(numero_passado, 2))

    return round(numero_passado, 2)

def subtrair():
    try:
        n1 = float(input('Digite o primeiro número: ')) 
        n2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')
    
    resultado = round(n1 - n2, 2)

    historico.append('Sub:')
    historico.append(resultado)
    return resultado

def multiplicar():
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')

    resultado = round(n1 * n2, 2)

    historico.append('Mult:')
    historico.append(resultado)
    return resultado

def dividir():
    try:
        n1 = float(input('Digite o dividendo: '))
        n2 = float(input('Digite o divisor: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')
    
    if n2 == 0:
        print('Um número não pode ser dividido por 0')
        return dividir()

    resultado = round(n1 / n2, 2)
    resto =  n1 % n2

    historico.append('D:')
    historico.append(resultado)
    return resultado, 'e o resto é:', resto

def potencia():
    try:
        n1 = float(input('Digite a base: '))
        n2 = float(input('Digite o exponete: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')

    resultado = round(pow(n1, n2), 2)

    historico.append('Pot:')
    historico.append(resultado)
    return resultado

def raiz():
    try:
        n1 = float(input('Digite o radicando: '))
        n2 = float(input('Digite o índice: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')
    
    resultado = round(pow(n1, 1/n2), 2)

    historico.append('R:')
    historico.append(resultado)
    return resultado

def porcentagem():
    try:
        n1 = float(input('Digite a taxa: '))
        n2 = float(input('Digite o todo(base): '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')

    resultado = round((n1/100) * n2, 2)

    historico.append('Por:')
    historico.append(resultado)
    return resultado

def media():
    try:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo número: '))
    except ValueError:
        print('Você digitou algo diferente de um número ou pode ter usado "," ao invés de "." para separar as casas decimais!')

    resultado = round((n1 + n2) / 2, 2)

    historico.append('Med: ')
    historico.append(resultado)
    return resultado

while True:
    numero_passado = 0
    n1 = 0
    n2 = 0
    print('------------------------------')
    print('[1] Realizar uma operação')
    print('[2] Ver histórico dos cálculos')
    print('[3] Limpar histórico')
    print('[0] Sair')
    print('------------------------------')

    acao_escolhida = input('O que você deseja fazer?: ')

    if acao_escolhida == '1':
        while True:
            print('------------------------------')
            print('[1] Adição')
            print('[2] Subtração')
            print('[3] Multiplicação')
            print('[4] Divisão - Resto')
            print('[5] Potenciação')
            print('[6] Radiciação')
            print('[7] Porcentagem')
            print('[8] Média')
            print('[0] Sair')
            print('------------------------------')

            tp_operacao = input('Qual operação será feita?: ')

            if tp_operacao == '1':
                resultado = somar()
                print(f'Resultado final da soma: {resultado}')
            elif tp_operacao == '2':
                resultado = subtrair()
                print(f'A diferença entre {n1} e {n2} é: {resultado}')
            elif tp_operacao == '3':
                resultado = multiplicar()
                print(f'A multiplicação entre {n1} e {n2} é: {resultado}')
            elif tp_operacao == '4':  
                resultado = dividir()              
                print(f'O quociente dessa divisão é: {resultado}')
            elif tp_operacao == '5':
                resultado = potencia()
                print(f'{n1} ^ {n2} é igual a potência de: {resultado}')
            elif tp_operacao == '6':     
                resultado = raiz()          
                print(f'A raiz de radicando {n1} no índice {n2} é: {resultado}')
            elif tp_operacao == '7':
                resultado = porcentagem()
                print(f'{n1}% de {n2} é: {resultado}')
            elif tp_operacao == '8':
                resultado = media()
                print(f'A média de {n1} e {n2} é: {resultado}')
            elif tp_operacao == '0':
                break
    elif acao_escolhida == '2':
        print(historico)
    elif acao_escolhida == '3':
        historico.clear()
    elif acao_escolhida == '0':
        break
    else:
        continue