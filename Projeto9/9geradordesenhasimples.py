import random

print('---Gerador de Senha simples---')

tmnh_senha = int(input('Qual o tamanho da senha que você quer gerar?'))
lista = list(['a', 1, 'h', '^', '°'])
senha = []

for i in range(tmnh_senha):
    senha.append(random.choices(lista))

#o map é usado no join quando tem elementos diferentes em uma lista
senha_real = "".join(map(str, senha))
print(senha_real)