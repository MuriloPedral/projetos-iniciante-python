import random

historico = []

MENU_PRINCIPAL = {
    1: 'Adivinhe um número de 0 até 1000',
    2: 'Histórico de Vitórias e Derrotas',
    3: 'Limpar Histórico',
    0: 'Sair'
}

DIFICULDADE = {
    'F': 12,
    'M': 10,
    'D': 8
}

def registrar_historico(historico, resultado, tentativas_restantes, dificuldade):
    registro = {
        'Resultado': resultado,
        'Tentativas Restantes': tentativas_restantes,
        'Dificuldade': dificuldade
    }
    historico.append(registro)

def exibir_historico():
    if not historico:
        print('Não tem histórico ainda.')
    else:
        for i, registro in enumerate(historico, start=1):
            print(f"{i}° rodada, Dificuldade: {registro['Dificuldade']} | {registro['Tentativas Restantes']} tentativas restantes | {registro['Resultado']}")

def exibir_placar(placar):
    print(f' ------ O placar atual está: {placar["vitorias"]} vitórias x {placar["derrotas"]} derrotas ------')

def deletar_historico():
    historico.clear()
    print('Histórico limpo.')

def escolher_dificuldade():
    while True:
        dificuldade = input(
            'Você quer qual dificuldade? '
            '[F] fácil, [M] médio ou [D] difícil: '
        ).strip().upper()

        if dificuldade in DIFICULDADE:
            return DIFICULDADE[dificuldade], dificuldade

        print('Você digitou algo diferente do esperado!')

def menu_principal():
    print('--------------------------------')
    print('---Jogo de Adivinhação part 2---')
    print('--------------------------------')
    
    for codigo, descricao in MENU_PRINCIPAL.items():
        print(f'[{codigo}] {descricao}')
    
    print('--------------------------------')

def validar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Você digitou algo diferente do esperado!')

def sortear_numero():
    return random.randint(0, 1000)

def reiniciar_valores():
    n_inicial = 0
    n_final = 1000
    return n_inicial, n_final

def validar_n_inserido(mensagem):
    while True:
        try:
            n_inserido = int(input(mensagem))
            if n_inserido > 1000:
                print('Você não pode digitar um número maior que 1000.')
            elif n_inserido < 0:
                print('Você não pode digitar um número menor que 0')
            elif 0 <= n_inserido <= 1000:
                return n_inserido 
        except ValueError:
            print('Digitou algo diferente do esperado')        

def registrar_vitorias_derrotas(venceu, placar):
    if venceu:
        placar['vitorias'] += 1
    else:
        placar['derrotas'] += 1

def venceu_derrotado(n_inserido, n_sorteado, n_tentativas):
    if n_inserido == n_sorteado:
        return f'Uhuu! Você acertou :) O número era: {n_sorteado}', True
    elif n_tentativas == 0:
        return f'Não foi dessa vez :(  O número era: {n_sorteado}', True
    
    return None, None

def maior_menor(n_inserido, n_sorteado, n_tentativas):
    if n_inserido > n_sorteado:
        return f'{n_inserido} é maior, tente um número menor. Você ainda tem: {n_tentativas} tentativas'
    elif n_inserido < n_sorteado:
        return f'{n_inserido} é menor, tente um número maior. Você ainda tem: {n_tentativas} tentativas'

def controle_n_mensagem(n_inserido, n_sorteado, n_inicial, n_final):
    if n_inserido > n_sorteado:
        if n_inserido < n_final:
            n_final = n_inserido
    elif n_inserido < n_sorteado:
        if n_inserido > n_inicial:
            n_inicial = n_inserido
    
    return n_inicial, n_final

def calculo_tentativas(n_tentativas):
    return n_tentativas - 1

def main():
    placar = {
        'vitorias': 0,
        'derrotas': 0
    }

    while True:
        menu_principal()
        acao_escolhida = validar_int('Escolha uma ação: ')

        if acao_escolhida == 1:
            n_tentativas, dificuldade_letra = escolher_dificuldade()
            n_sorteado = sortear_numero()
            n_inicial, n_final = reiniciar_valores()
            while True:
                n_inserido = validar_n_inserido(f'Digite um número entre {n_inicial} e {n_final}: ')

                n_tentativas = calculo_tentativas(n_tentativas)
                resultado, sair_loop = venceu_derrotado(n_inserido, n_sorteado, n_tentativas)
                if sair_loop:
                    venceu = (n_inserido == n_sorteado)
                    registrar_vitorias_derrotas(venceu, placar)
                    registrar_historico(historico, 'Vitória' if venceu else 'Derrota', n_tentativas, dificuldade_letra)
                    print(resultado)
                    break

                print(maior_menor(n_inserido, n_sorteado, n_tentativas))
                n_inicial, n_final = controle_n_mensagem(
                    n_inserido, n_sorteado, n_inicial, n_final
                )

        elif acao_escolhida == 2:
            exibir_placar(placar)
            exibir_historico()
        elif acao_escolhida == 3:
            deletar_historico()
        elif acao_escolhida == 0:
            break

if __name__ == '__main__':
    main()