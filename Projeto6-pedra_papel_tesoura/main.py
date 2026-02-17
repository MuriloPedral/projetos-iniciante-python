import random

print('---Olá, seja bem vindo!---')
print('Pronto para jogar Jokenpô?')
print('--------------------------')

continuar_jogando = False
OPCOES = ['pedra', 'papel', 'tesoura']
placar_v = 0
placar_d = 0
placar_e = 0

while not continuar_jogando:
    resposta = str(input('Pedra, papel ou tesoura?: ').lower())
    if resposta == 'pedra' or resposta == 'papel' or resposta == 'tesoura':

        resposta_computador = random.choice(OPCOES)

        ganhar = (resposta == 'pedra' and resposta_computador == 'tesoura') or (resposta == 'papel' and resposta_computador == 'pedra') or (resposta == 'tesoura' and resposta_computador == 'papel')
        perder = (resposta == 'pedra' and resposta_computador == 'papel') or (resposta == 'papel' and resposta_computador == 'tesoura') or (resposta == 'tesoura' and resposta_computador == 'pedra')
        empate = resposta == resposta_computador

        if ganhar:
            print('Ganhou')
            placar_v = placar_v + 1
        elif perder:
            print('Perdeu')
            placar_d = placar_d + 1
        elif empate:
            print('Empatou')
            placar_e = placar_e + 1

        placar = [placar_v, placar_d, placar_e]
        print(f'Placar atual, Vitórias: {placar[0]} | Derrotas: {placar[1]} | Empates: {placar[2]}')

        continuar = int(input('Quer continuar jogando? [1] para sim e [2] para não: '))        
        if continuar == 1:
            continuar_jogando = False        
        elif continuar == 2:
            continuar_jogando = True
        else:
            print('Você digitou algo diferente de 1 ou 2, então iremos considerar que você queira jogar mais uma vez!')  
    else:
        print('Você digitou algo errado!')