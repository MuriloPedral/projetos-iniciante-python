IDADE_MINIMA = 0
ADOLESCENTE = 12
ADULTO = 20
IDOSO = 60
IDADE_IRREAL = 130
MENOR_IDADE = []
MAIOR_IDADE = []

BR_MAIOR_IDADE = 18
print('-------------------------------------------------')
print('Verificador de faixa etária baseado na OMS - 2026')

while True:
    print('-------------------------------------------------------------')
    print('[1] para digitar uma idade')
    print('[2] para ver as métricas utilizadas')
    print('[3] para ver quantidade de maior e menor de idade adicionados')
    print('[0] par sair')
    print('-------------------------------------------------------------')

    acao_escolhida = input('O que você gostaria de fazer?: ')

    if acao_escolhida == '1':
        idade = input('Qual a idade que você gostaria de verificar?: ')
        if idade.isdigit():
            idade = int(idade)
            if idade >= IDADE_MINIMA and idade <= IDADE_IRREAL:
                if idade >= IDADE_MINIMA and idade < ADOLESCENTE:
                    print(f'Atualmente de acordo com a OMS, uma pessoa com {idade} anos é considerada criança.')
                elif idade >= ADOLESCENTE and idade < ADULTO:
                    print(f'Atualmente de acordo com a OMS, uma pessoa com {idade} anos é considerada adolescente.')
                elif idade >= ADULTO and idade < IDOSO:
                    print(f'Atualmente de acordo com a OMS, uma pessoa com {idade} anos é considerada adulto.')
                elif idade >= IDOSO:
                    print(f'Atualmente de acordo com a OMS, uma pessoa com {idade} anos é considerada idoso.')

                if idade < BR_MAIOR_IDADE:
                    MENOR_IDADE.append(idade)
                elif idade >= BR_MAIOR_IDADE:
                    MAIOR_IDADE.append(idade)            
            else:
                print('Digitou uma idade irreal!')

        else:
            print('Você digitou algo diferente de um número.')
    elif acao_escolhida == '2':
        print('-------------------------------------------------------------')
        print(f'Considera-se criança dos {IDADE_MINIMA} aos {ADOLESCENTE} anos incompletos. - 2026 OMS')
        print(f'Considera-se adolescente dos {ADOLESCENTE} aos {ADULTO} anos incompletos. - 2026 OMS')
        print(f'Considera-se adulto dos {ADULTO} aos {IDOSO} anos incompletos. - 2026 OMS')
        print(f'Considera-se idoso a partir dos {IDOSO} anos . - 2026 OMS')
        print(f'No brasil a maior idade corresponde aos {BR_MAIOR_IDADE} anos. - 2026 LEGISLAÇÃO BRASILEIRA')
    elif acao_escolhida == '3':
        print(f'Foram {len(MAIOR_IDADE)} pessoas maior de idade, elas foram: {MAIOR_IDADE}')
        print(f'Foram {len(MENOR_IDADE)} pessoas menor de idade, elas foram: {MENOR_IDADE}')
    elif acao_escolhida == '0':
        break
    else:
        print('Você digitou algo diferente do esperado.')
        continue

