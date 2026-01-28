print('---Média de notas---')

n = 0

qnt_notas = int(input('Quantas notas você gostaria de calcular a média?: '))

for i in range(qnt_notas):
    ni = float(input(f'Digite a {i}° nota: '))
    n = ni + n

m = n / qnt_notas

if m >= 7 and m <= 10:
    print(f'Essa é a média: {m: .2f}, parabéns, está aprovado!')
elif m < 7 and m >= 0:
    print(f'Essa é a média: {m: .2f}, infelizmente você foi reprovado!')

#pode usar essa formatação para arrendondar o número
#round(m, 2)