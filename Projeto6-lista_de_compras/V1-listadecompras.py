print('---Lista de Compras---')

nm = str(input('Qual o seu nome?: '))

lista = list([])
el_lista = 'a'

while el_lista == 'a' or el_lista == 'r' or el_lista == 'v':
    el_lista = input('Você gostaria de adicionar [A], remover [R] ou ver [V] sua lista, ou deseja sair do programa [sair]?: ').lower()
    if el_lista == 'a':
        lista.append(input('Adicione: ').lower())
    elif el_lista == 'r':
        print(lista)
        lista.remove(input('Remova: ').lower())
    elif el_lista == 'v':
        print(f'{nm}, a sua lista de compras, está assim: {lista}')

#del tira o elemento baseado na posição
#del lista[]
#pop tira o último elemento da lista
#lista.pop()
#remove você escolhe o que está na lista que você vai tirar
#lista.remove()