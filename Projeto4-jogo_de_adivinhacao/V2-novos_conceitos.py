import random

print('---Jogo de Adivinhação part 2---')
print('Advinhe um número de 0 até 100')

n_sorteado = random.randint(0, 1000)
continuar = True
dificuldade_escolhida = False

while continuar == True:
    while dificuldade_escolhida == False:
        dificuldade = input('Você quer qual dificuldade? [F] para fácil, [M] para médio ou [D] para difícil: ').upper()

        n_sorteado = random.randint(0, 1000)

        if dificuldade == 'F':
            lim_tentativas = 15
            dificuldade_escolhida = True
        elif dificuldade == 'M':
            lim_tentativas = 10
            dificuldade_escolhida = True
        elif dificuldade == 'D':
            lim_tentativas = 5
            dificuldade_escolhida = True
        else:
            print('Você digitou algo diferente do esperado, estamos reiniciando o programa...')
            continue

    palpite = int(input('Digite um número: '))
    
    if palpite >= 0 and palpite <= 1000:
        lim_tentativas = lim_tentativas - 1
        print(f'Você ainda tem {lim_tentativas} tentativas')

        if palpite < n_sorteado:
            print('Digite um número maior')
        elif palpite > n_sorteado:
            print('Digite um número menor')
        elif palpite == n_sorteado:
            print(f'Uhuu! Você acertou :) O número era: {n_sorteado}')
        
        if lim_tentativas == 0:
            print(f'Não foi dessa vez :(  O número era: {n_sorteado}')

    if lim_tentativas == 0 or palpite == n_sorteado:
        tentar_dnv = input('Deseja jogar mais uma vez? (s/n): ').lower()
        if tentar_dnv == 's':
            dificuldade_escolhida = False
            dificuldade = ''
        elif tentar_dnv == 'n':
            continuar = False
        else:
            break