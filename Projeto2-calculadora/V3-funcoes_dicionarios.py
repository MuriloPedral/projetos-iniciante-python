import math

historico = []

OPERACOES = {
    1: 'Adição',
    2: 'Subtração',
    3: 'Multiplicação',
    41: 'Divisão',
    42: 'Resto',
    5: 'Potenciação',
    6: 'Radiciação',
    7: 'Porcentagem',
    8: 'Média',
    91: 'Grau para Radianos',
    92: 'Seno', 
    93: 'Cosseno',
    94: 'Tangente',
    10: 'Pi',
    11: 'Logaritmos',
    12: 'Euler',
    13: 'Logaritmo Natural',
}

MENU_PRINCIPAL = {
    1: 'Realizar uma operação',
    2: 'Ver histórico dos cálculos',
    3: 'Limpar histórico',
    0: 'Sair'
}   

MENU_OPERACOES = {
    1: 'Adição',
    2: 'Subtração',
    3: 'Multiplicação',
    4: 'Divisão',
    5: 'Potenciação',
    6: 'Radiciação',
    7: 'Porcentagem',
    8: 'Média',
    9: 'Seno, Cosseno, Tangente', 
    10: 'Pi',
    11: 'Logaritmos',
    12: 'Euler',
    13: 'Logaritmo Natural',
}

MENU_TRIGONOMETRIA = {
    1: 'Transformar de grau para radiano',
    2: 'Calcular seno',
    3: 'Calcular cosseno',
    4: 'Calcular tangente',
    0:  'Sair'
}

def registro_operacoes(codigo_operacao, resultado):
    registro = {
        'Operação': OPERACOES.get(codigo_operacao, 'Operação desconhecida'), 
        'Resultado': resultado
        }
    historico.append(registro)

def exibir_historico():
    if not historico:
        print('Ainda não há histórico.')
    else:
        for i, registro in enumerate(historico, start=1):
            print(f"{i}° registro: {registro['Operação']} com resultado → {registro['Resultado']}")

def limpar_historico():
    historico.clear()
    print('Histórico limpo com sucesso.')

def validar_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print('Digite um número inteiro válido!')

def validar_mensagem(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Você digitou algo diferente de um número!')

def menu_principal():
    print('------------------------------')
    print('         CALCULADORA')
    print('------------------------------')

    for codigo, descricao in MENU_PRINCIPAL.items():
        print(f'[{codigo}] {descricao}')

    print('------------------------------')

def menu_operacoes():   
    print('------------------------------')

    for codigo, descricao in MENU_OPERACOES.items():
        print(f'[{codigo}] {descricao}')

    print('------------------------------')

def menu_trigonometria():
    print('------------------------------')
    print('         TRIGONOMETRIA')
    print('------------------------------')
    
    for codigo, descricao in MENU_TRIGONOMETRIA.items():
        print(f'[{codigo}] {descricao}')

    print('------------------------------')

def um_numero(msg1):
    n1 = validar_mensagem(msg1)
    return n1

def dois_numeros(msg1, msg2):
    n1 = validar_mensagem(msg1)
    n2 = validar_mensagem(msg2)
    return n1, n2

def reduzir_casas_decimais(operacao):
    return round(operacao, 3)

def soma_operacao():
    soma = 0
    while True:
        numero = validar_mensagem('Digite um número: ')
        soma = numero + soma
        continuar_soma = input('Você gostaria de continuar somando? [s/n]').lower()
        if continuar_soma != 's':
            break

    codigo_operacao = 1
    resultado = reduzir_casas_decimais(soma)
    return codigo_operacao, resultado

def subtracao_operacao(n1, n2):
    codigo_operacao = 2
    resultado = reduzir_casas_decimais(n1 - n2)

    return codigo_operacao, resultado

def multiplicacao_operacao(n1, n2):
    codigo_operacao = 3
    resultado = reduzir_casas_decimais(n1 * n2)

    return codigo_operacao, resultado

def divisao_valida(n2):
    return n2 != 0

def divisao_operacao(n1, n2):
    codigo_operacao = 41
    resultado = reduzir_casas_decimais(n1 / n2)

    return codigo_operacao, resultado

def divisao_resto(n1, n2):
    codigo_operacao = 42
    resultado = reduzir_casas_decimais(n1 % n2)

    return codigo_operacao, resultado

def exponencial_valido(n1, n2):
    if n1 == 0 and n2 == 0:
        return False, 'Indeterminado (0⁰)'
    elif n1 == 0 and n2 < 0:
        return False, 'Impossível (divisão por zero)'
    elif n1 < 0 and n2 != int(n2):
        return False, 'Base negativa com expoente fracionário não é real'
    return True, None

def potenciacao_operacao(n1, n2):
    codigo_operacao = 5
    resultado = reduzir_casas_decimais(pow(n1, n2))

    return codigo_operacao, resultado

def raiz_valida(n1, n2):
    if n2 < 0 and n1 % 2 == 0:
        return False, 'Impossível nos número Reais.'
    return True, None

def raiz_operacao(n1, n2):
    codigo_operacao = 6
    resultado = reduzir_casas_decimais(pow(n2, 1 / n1))

    return codigo_operacao, resultado

def porcentagem_operacao(n1, n2):
    codigo_operacao = 7
    resultado = reduzir_casas_decimais(n1 * (n2/100))

    return codigo_operacao, resultado

def media_operacao(n1, n2):
    codigo_operacao = 8
    resultado = reduzir_casas_decimais((n1 + n2)/2)

    return codigo_operacao, resultado

def grau_para_radiano(n1):
    codigo_operacao = 91
    resultado = n1 * math.pi / 180

    return codigo_operacao, resultado

def grau_para_radiano_valor(n1):
    return n1 * math.pi / 180

def seno_operacao(n1):
    codigo_operacao = 92

    angulo_rad = grau_para_radiano_valor(n1)
    resultado = reduzir_casas_decimais(math.sin(angulo_rad))

    return codigo_operacao, resultado  

def cosseno_operacao(n1):
    codigo_operacao = 93

    angulo_rad = grau_para_radiano_valor(n1)
    resultado = reduzir_casas_decimais(math.cos(angulo_rad))
    
    return codigo_operacao, resultado

def tangente_valido(n1):
    angulo_rad = grau_para_radiano_valor(n1)
    if math.isclose(math.cos(angulo_rad), 0.0, abs_tol=1e-9):
        return False, 'Tangente indefinida (cosseno = 0)'
    return True, None

def tangente_operacao(n1):
    codigo_operacao = 94

    angulo_rad = grau_para_radiano_valor(n1)
    resultado = reduzir_casas_decimais(math.tan(angulo_rad))

    return codigo_operacao, resultado

def pi_operacao(n1):
    codigo_operacao = 10
    resultado = math.pi * n1

    return codigo_operacao, resultado

def logaritmo_valido(n1, n2):
    if n1 <= 0:
        return False, 'O logaritmando deve ser maior que 0.'
    if n2 <= 0 or n2 == 1:
        return False, 'A base deve ser maior que 0 e diferente de 1.'
    
    return True, None

def logaritmo_operacao(n1, n2):
    codigo_operacao = 11
    resultado = reduzir_casas_decimais(math.log(n1, n2))

    return codigo_operacao, resultado

def euler_operacao(n1):
    codigo_operacao = 12
    resultado = math.e * n1

    return codigo_operacao, resultado

def ln_valido(n1):
    if n1 <= 0:
        return False, 'O valor deve ser maior que 0.'
    return True, None

def ln_operacao(n1):
    codigo_operacao = 13
    resultado = reduzir_casas_decimais(math.log(n1))

    return codigo_operacao, resultado

def main():
    while True:
        menu_principal()
        decisao_acao = validar_int('Qual ação você quer fazer?: ')

        if decisao_acao == 1:
            menu_operacoes()
            decisao_operacoes = validar_int('Qual operação você quer fazer?: ')

            if decisao_operacoes == 1:
                codigo, resultado = soma_operacao()
                registro_operacoes(codigo, resultado)
                print(f'A soma de todos os números é: {resultado}')

            elif decisao_operacoes == 2:
                n1, n2 = dois_numeros(
                    'Digite o primeiro número: ',
                    'Digite o segundo número: '
                )
                codigo, resultado = subtracao_operacao(n1, n2)
                registro_operacoes(codigo, resultado)
                print(f'{n1} menos {n2} é: {resultado}')

            elif decisao_operacoes == 3:
                n1, n2 = dois_numeros(
                    'Digite o primeiro fator: ',
                    'Digite o segundo fator: '
                )
                codigo, resultado = multiplicacao_operacao(n1, n2)
                registro_operacoes(codigo, resultado)
                print(f'{n1} multiplicado por {n2} é: {resultado}')

            elif decisao_operacoes == 4:
                n1, n2 = dois_numeros(
                    'Digite o dividendo: ',
                    'Digite o divisor: '
                )
                if not divisao_valida(n2):
                    print('Não é possível dividir por 0.')
                else:
                    codigo, resultado = divisao_operacao(n1, n2)
                    registro_operacoes(codigo, resultado)
                    print(f'{n1} dividido por {n2} é: {resultado}')

                    codigo, resultado = divisao_resto(n1, n2)
                    registro_operacoes(codigo, resultado)
                    print(f'{n1} dividido por {n2} é: {resultado}')

            elif decisao_operacoes == 5:
                n1, n2 = dois_numeros(
                    'Digite a base: ',
                    'Digite o expoente: '
                )
                valido, erro = exponencial_valido(n1, n2)
                if not valido:
                    print(f'Erro: {erro}')
                else:
                    codigo, resultado = potenciacao_operacao(n1, n2)
                    registro_operacoes(codigo, resultado)
                    print(f'{n1} elevado a {n2} é: {resultado}')

            elif decisao_operacoes == 6:
                n1, n2 = dois_numeros(
                    'Digite o índice: ',
                    'Digite o radicando: '
                )
                valido, erro = raiz_valida(n1, n2)
                if not valido:
                    print(f'Erro: {erro}')
                else:
                    codigo, resultado = raiz_operacao(n1, n2)
                    registro_operacoes(codigo, resultado)
                    print(f'A raiz de {n2} no índice {n1} é: {resultado}')

            elif decisao_operacoes == 7:
                n1, n2 = dois_numeros(
                    'Digite a base: ',
                    'Digite a taxa: '
                )
                codigo, resultado = porcentagem_operacao(n1, n2)
                registro_operacoes(codigo, resultado)
                print(f'{n2}% de {n1} equivale a: {resultado}')

            elif decisao_operacoes == 8:
                n1, n2 = dois_numeros(
                    'Digite o primeiro número:',
                    'Digite o segundo número: '
                )
                codigo, resultado = media_operacao(n1, n2)
                registro_operacoes(codigo, resultado)
                print(f'A média entre {n1} e {n2} é: {resultado}')

            elif decisao_operacoes == 9:
                menu_trigonometria()
                decidir_trigonometria = validar_int('Qual operação você quer fazer?: ')

                if decidir_trigonometria == 1:
                    n1 = um_numero(
                        'Digite o grau(ângulo) para transformar em radianos: '
                        )
                    codigo, resultado = grau_para_radiano(n1)
                    registro_operacoes(codigo, resultado)
                    print(f'O ângulo de {n1}° tem radiano igual a: {resultado}')

                elif decidir_trigonometria == 2:
                    n1 = um_numero(
                        'Digite o ângulo para calcular o seno: '
                        )
                    codigo, resultado = seno_operacao(n1)
                    registro_operacoes(codigo, resultado)
                    print(f'O ângulo de {n1}° tem seno igual a: {resultado}')

                elif decidir_trigonometria == 3:
                    n1 = um_numero(
                        'Digite o ângulo para calcular o cosseno: '
                        )
                    codigo, resultado = cosseno_operacao(n1)
                    registro_operacoes(codigo, resultado)
                    print(f'O ângulo de {n1}° tem cosseno igual a: {resultado}')

                elif decidir_trigonometria == 4:
                    n1 = um_numero(
                        'Digite o ângulo para calcular a tangente: '
                        )
                    valido, erro = tangente_valido(n1)
                    if not valido:
                        print(f'Erro: {erro}')
                    else:
                        codigo, resultado = tangente_operacao(n1)
                        registro_operacoes(codigo, resultado)
                        print(f'O ângulo de {n1}° tem tangente igual a: {resultado}')

                else:
                    print('Saindo...')
                    break

            elif decisao_operacoes == 10:
                n1 = um_numero(
                    'Digite um número para multiplicar por Pi: '
                    )
                codigo, resultado = pi_operacao(n1)
                registro_operacoes(codigo, resultado)
                print(f'{n1} vezes Pi aproximado é: {resultado}')

            elif decisao_operacoes == 11:
                n1, n2 = dois_numeros(
                    'Digite o logaritmando:',
                    'Digite a base:'
                )
                valido, erro = logaritmo_valido(n1, n2)
                if not valido:
                    print(f'Erro: {erro}')
                else:
                    codigo, resultado = logaritmo_operacao(n1, n2)
                    registro_operacoes(codigo, resultado)
                    print(f'O logaritmo de {n1} na base {n2} é igual a: {resultado}')

            elif decisao_operacoes == 12:
                n1 = um_numero(
                    'Digite um número para multiplicar por Euler: '
                    )
                codigo, resultado = euler_operacao(n1)
                registro_operacoes(codigo, resultado)
                print(f'{n1} vezes Euler é: {resultado}')

            elif decisao_operacoes == 13:
                n1 = um_numero(
                    'Digite o logaritmando para calcular o LN: '
                    )
                valido, erro = ln_valido(n1)
                if not valido:
                    print(f'Erro: {erro}')
                else:
                    codigo, resultado = ln_operacao(n1)
                    registro_operacoes(codigo, resultado)
                    print(f'O valor de LN({n1}) é: {resultado}')

            elif decisao_operacoes == 0:
                break

        elif decisao_acao == 2:
            exibir_historico()
        elif decisao_acao == 3:
            limpar_historico()
        elif decisao_acao == 0:
            print('Obrigado por usar minha calculadora!')
            break

if __name__ == '__main__':
    main()