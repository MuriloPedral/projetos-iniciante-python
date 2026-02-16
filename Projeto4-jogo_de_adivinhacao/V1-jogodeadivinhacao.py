import random

print('---Bem-Vindo ao jogo da adivinhação---')


ninicial = int(input('Digite um número inteiro inicial entre 1 e 100: '))

#random.radint(1, 100) faz com que gera um número aleatório inteiro entre 1 e 100
#random.random() que gera número decimal entre 0.0 e 1.0
#random.choice(nomedavariavel) faz o sorteio de uma lista
nsorteado = random.randint(1, 100)


if ninicial > 100 or ninicial < 1:
    print('Você digitou um número fora do range')
elif nsorteado == ninicial:
    print('Você acertou!')
elif ninicial != nsorteado:
    while ninicial != nsorteado:
        if ninicial > nsorteado:
            ninicial = int(input('Digite um número menor: '))
        elif ninicial < nsorteado:
            ninicial = int(input('Digite um número maior: '))
        else:
            print('Não sei o que pode dar diferente disso')
        
        if ninicial == nsorteado:
            print('Você acertou!')
else:
    print('Deu algum erro')