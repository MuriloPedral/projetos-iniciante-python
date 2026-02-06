historico = []

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Você digitou algo diferente de um número, tente novamente.')

def menu_principal():   
    print('--------------------')
    print('[1] Nova Soma')
    print('[2] Ver Histórico')
    print('[3] Limpar Histórico')
    print('[0] Sair')
    print('--------------------')
    decisao_acao = input('Digite o valor correspondente à ação desejada [0-3]: ')
    return decisao_acao

def menu_soma():
    print('------------------------------------------')
    print('[1] Somar quantidade específica de números')
    print('[2] Somar quantos números quiser')
    print('[0] Sair')
    print('------------------------------------------')
    decisao_soma = input('Digite o valor correspondente à ação desejada [0-2]: ')
    return decisao_soma

# Função genérica para registrar soma no histórico
def registrar_soma(numeros_operacao):
    """
    Recebe uma lista de números, calcula a soma e adiciona ao histórico.
    Retorna a soma calculada.
    """
    soma = sum(numeros_operacao)  # usa sum() em vez de loop manual
    historico.append({'numeros': numeros_operacao, 'soma': soma})  # cada operação é um dicionário
    return soma

def somar_quantidade_fixa(qnt_numeros):
    numeros_atual = []
    for i in range(qnt_numeros):
        numero = ler_numero(f'Digite o {i + 1}° número: ')
        numeros_atual.append(numero)
    soma = registrar_soma(numeros_atual)  # registra no histórico
    return soma

def somar_quantidade_livre():
    numeros_atual = []
    while True:
        numero = ler_numero('Digite um número para somar: ')
        numeros_atual.append(numero)
        continuar = input('Quer somar mais um número? [s/n] ').lower()
        if continuar != 's':
            break
    soma = registrar_soma(numeros_atual)  # registra no histórico
    return soma

while True:
    decisao_acao = menu_principal()

    if decisao_acao == '1':
        decisao_soma = menu_soma()

        if decisao_soma == '1':
            try:
                qnt_numeros = int(input('Quantos números você quer somar?: '))
            except ValueError:
                print('Você digitou algo diferente do número esperado!')
                continue
            soma = somar_quantidade_fixa(qnt_numeros)
            print(f'Essa é a soma final: {soma}')

        elif decisao_soma == '2':
            soma = somar_quantidade_livre()
            print(f'Essa é a soma final: {soma}')
        elif decisao_soma == '0':
            print('Saindo...')
        else:
            print('Você digitou algo diferente do número esperado!')

    elif decisao_acao == '2':
        if not historico:
            print('Ainda não há histórico.')
        else:
            for i, operacao in enumerate(historico):
                print(f'A {i + 1}° soma entre os números {operacao["numeros"]} foi: {operacao["soma"]}')

    elif decisao_acao == '3':
        historico.clear()
        print('Histórico limpo com sucesso.')

    elif decisao_acao == '0':
        print('Obrigado por utilizar o programa!')
        break

    else:
        print('Você digitou algo diferente do esperado! Digite novamente...')
