LISTA_GLOBAL = []

#Entender melhor esse while True
while True:
    LOOP_SOMA = False
    MAIS_NUMERO = True

    print('--------------------')
    print('[1] Nova Soma')
    print('[2] Ver Histórico')
    print('[3] Limpar Histórico')
    print('[0] Sair')
    print('--------------------')

    escolha = input('Qual é a próxima ação?: ')

    if escolha == '1':
        LISTA_NUMERO = []
        LISTA_SOMA = []

        while LOOP_SOMA == False:
            print('------------------------------------------')
            print('[1] Somar quantidade específica de números')
            print('[2] Somar quantos números quiser')
            print('[0] Sair')
            print('------------------------------------------')

            tp_soma = input('Qual operação você quer fazer?: ')

            if tp_soma.isdigit():
                tp_soma = int(tp_soma)

                NUMERO1_NOVO = 0
                numero = 0
                soma = 0

                if tp_soma == 1:
                    try:
                        qnt_numeros = int(input('Quantos números você quer somar?: '))
                    except ValueError:
                        print('Você digitou algo totalmente fora do inesperado')
                        continue
                    for i in range(qnt_numeros):
                        try:
                            numero = int(input(f'Digite o {i + 1}° número: '))
                        except ValueError:
                            print('Você não digitou um número.')
                            continue
                        soma = numero + NUMERO1_NOVO
                        print(f'A soma de {numero} + {NUMERO1_NOVO} é igual a:', soma)                
                        NUMERO1_NOVO = soma
                        LISTA_NUMERO.append(numero)
                    print(f'A soma final é: {soma}')
                    LOOP_SOMA = True
                elif tp_soma == 2:
                    while MAIS_NUMERO == True:
                        quer_Mnumero = input('Quer adicionar um número? [s/n]: ')
                        if quer_Mnumero == 's':
                            try:
                                numero = int(input('Digite um número: '))
                                soma = numero + NUMERO1_NOVO
                                print(f'A soma de {numero} + {NUMERO1_NOVO} é igual a:', soma)
                                NUMERO1_NOVO = soma
                                LISTA_NUMERO.append(numero)
                            except ValueError:
                                print('Você digitou algo totalmente fora do inesperado!')
                                continue
                        elif quer_Mnumero == 'n':
                            MAIS_NUMERO = False
                        else:
                            continue
                    print(f'A soma final é: {soma}')
                    LOOP_SOMA = True
                elif tp_soma == 0:
                    LOOP_SOMA = True
                else:
                    print('Algo de inesperado foi digitado!')
                    continue
            else:
                print('Algo de inesperado foi digitado!')
                continue
            LISTA_SOMA.append(soma)
        if LISTA_NUMERO:
            LISTA_GLOBAL.append(LISTA_NUMERO)
            LISTA_GLOBAL.append('-> Soma:')
            LISTA_GLOBAL.append(LISTA_SOMA)
    elif escolha == '2':

        #Estudar o que esse enumerate faz e entender melhor essa lógica
        if LISTA_GLOBAL == []:
            print('----------------------')
            print('A sua lista está vazia')
            print('----------------------')
        else:
            print('-----------------')
            for i, item in enumerate(LISTA_GLOBAL):
                print(item, end="")
                if (i + 1) % 3 == 0:
                    print()
            print('-----------------')
    elif escolha == '3':
        LISTA_SOMA = []
        LISTA_NUMERO = []
        LISTA_GLOBAL = []
    elif escolha == '0':
        print('Você decidiu sair do programa, espero que tenha gostado!')
        break
    else:
        print('Você digitou um valor diferente do esperado, tente mais uma vez!')
        continue