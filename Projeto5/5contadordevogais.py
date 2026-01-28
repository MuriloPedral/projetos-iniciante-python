print('---Contador de vogais---')

palavra = str(input('Digite uma PALAVRA: ')).lower()
lista_vogais = list(['a', 'e', 'i', 'o', 'u'])

indice = 0
indice2 = 0
qnt_vogais = 0

#nesse código ele contou a quantidade de letras em uma string:    tamanho_palavra = len(palavra)

#transforma a palavra em lista
palavra = list(palavra)

#esse loop começa com o len para contar a quantidade de letras na palavra e o indice com valor 0 permite ele percorrer de 0 até o tamanho da palavra
#eu consegui fazer que a variavel letra retornasse cada letra da palavra usando como parâmetro o índice, então como palavra é uma lista antes de 
#entrar no loop, ele perccore palavra[0]... que justamente é retornar cada elemento de uma lista e no segundo loop ele tem uma idea parecida que
#ele percorre a lista de vogais com a mesma lógica de indice, e no fim tem um if para comparar se a primeira letra da palavra fica comparando
#com cada vogal que tá na lista de vogais, se tiver ele conta, se não tiver ele percorre todas as vogais e saí do segundo loop e volta para o primeiro
for indice in range(len(palavra)):
    letras = palavra[indice]
    for indice2 in range(len(lista_vogais)):
        #print(lista_vogais[indice2])
        vogal = lista_vogais[indice2]
        if letras == vogal:
            qnt_vogais = qnt_vogais + 1

#exemplo de retorno de um elemento dentro de uma lista
#print(str(lista_vogais[0]))

#o comando .join faz que você possa transformar uma lista em uma string
voltando_palavra = "".join(palavra)
print(f'A palavra {voltando_palavra}, tinha {qnt_vogais}, vogais.')