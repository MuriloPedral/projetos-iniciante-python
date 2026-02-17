MENU_PRINCIPAL = {
    1: 'Calcular média aritmética simples',
    2: 'Calcular média aritmética ponderada',
    3: 'Ver histórico de média',
    4: 'Deletar histórico',
    0: 'Sair'
}

def menu_principal():
    print('-------------------------------')
    print('Calculadora de média aritmética')
    print('-------------------------------')

    for i, valor in MENU_PRINCIPAL.items():
        print(f'[{i}] {valor}')

    print('-------------------------------')

def registrar_historico(historico, media, tipo_media):
    registro = {
        'media': media,
        'tipo': tipo_media
    }
    historico.append(registro)

def exibir_historico(historico):
    if not historico:
        print('Ainda não tem histórico')
    else:
        for i, registro in enumerate(historico, start=1):
            print(f'{i}° tem média igual a: {registro["media"]}, tipo: {registro["tipo"]}')

def limpar_historico(historico):
    historico.clear()
    print('Histórico limpo com sucesso!')

def validar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Você digitou algo diferente do esperado!')

def validar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Você digitou algo diferente do esperado!')

def continuar_calculo():
    continuar = input('Continuar adicionando número? [S]im ou [N]ão: ').lower()

    if continuar == 'n':
        return False
    
    return True

def registrar_numerador(numerador_lista, numero):
    numerador_lista.append(numero)

def registrar_peso(peso_lista, peso):
    peso_lista.append(peso)

def calcular_media_simples(numerador_lista):
    if not numerador_lista:
        raise ValueError("Lista vazia.")

    return sum(numerador_lista) / len(numerador_lista)

def calcular_media_ponderada(numerador_lista, peso_lista):
    soma_produtos = 0
    soma_pesos = 0

    for numero, peso in zip(numerador_lista, peso_lista):
        soma_produtos += numero * peso
        soma_pesos += peso

    if soma_pesos == 0:
        raise ValueError("A soma dos pesos não pode ser zero.")

    return soma_produtos / soma_pesos


def main():
    historico = []
    while True:
        numerador_lista = []
        peso_lista = []

        menu_principal()
        decisao = validar_int('Digite um valor: ')

        if decisao == 1:
            tipo_media = 'Simples'
            while True:
                numero = validar_float('Digite o número para calcular a média: ')

                registrar_numerador(numerador_lista, numero)

                continuar = continuar_calculo()
                if not continuar:
                    media = calcular_media_simples(numerador_lista)
                    registrar_historico(historico, media, tipo_media)

                    print(f'A média dos números é igual a: {media}')
                    break

        elif decisao == 2:
            tipo_media = 'Ponderada'
            while True:
                numero = validar_float('Digite o número para calcular a média: ')
                peso = validar_float(f'Digite o peso de {numero}: ')

                registrar_numerador(numerador_lista, numero)
                registrar_peso(peso_lista, peso)

                continuar = continuar_calculo()
                if not continuar:
                    media = calcular_media_ponderada(numerador_lista, peso_lista)
                    registrar_historico(historico, media, tipo_media)

                    print(f'A média dos números é igual a: {media}')
                    break

        elif decisao == 3:
            exibir_historico(historico)
        elif decisao == 4:
            limpar_historico(historico)
        elif decisao == 0:
            print('Obrigado por utilizar o programa.')
            break

if __name__ == '__main__':
    main()