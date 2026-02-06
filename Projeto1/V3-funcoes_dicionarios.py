IDADE_MINIMA = 0
ADOLESCENTE = 12
ADULTO = 20
IDOSO = 60
IDADE_IRREAL = 130
BR_MAIOR_IDADE = 18
historico = []

def validar_mensagem(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.strip() == '':
            print('Você não digitou nada! Tente novamente.')
            continue
        try:
            return int(entrada)
        except ValueError:
            print('Você digitou algo diferente do esperado! Tente novamente.')

def menu_principal():
    print('-------------------------------------------------')
    print('Verificador de faixa etária baseado na OMS - 2026')
    print('-------------------------------------------------')
    print('[1] Digitar uma idade')
    print('[2] Ver as métricas utilizadas')
    print('[3] Ver histórico')
    print('[4] Apagar histórico')
    print('[0] Sair')
    print('-------------------------------------------------')
    return validar_mensagem('Digite a ação: ')

def faixa_etaria(idade):
    if IDADE_MINIMA <= idade < ADOLESCENTE:
        return 'Criança'
    elif ADOLESCENTE <= idade < ADULTO:
        return 'Adolescente'
    elif ADULTO <= idade < IDOSO:
        return 'Adulto'
    elif IDOSO <= idade < IDADE_IRREAL:
        return 'Idosa'
    else:
        return 'Idade inválida'

def metricas():
    print(f'Considera-se criança dos {IDADE_MINIMA} aos {ADOLESCENTE} anos incompletos. - 2026 OMS')
    print(f'Considera-se adolescente dos {ADOLESCENTE} aos {ADULTO} anos incompletos. - 2026 OMS')
    print(f'Considera-se adulto dos {ADULTO} aos {IDOSO} anos incompletos. - 2026 OMS')
    print(f'Considera-se idoso a partir dos {IDOSO} anos. - 2026 OMS')
    print(f'No brasil a maior idade corresponde aos {BR_MAIOR_IDADE} anos. - 2026 LEGISLAÇÃO BRASILEIRA')

def maior_idade(idade):
    if idade >= BR_MAIOR_IDADE:
        return 'Maior de Idade'
    else: 
        return 'Menor de Idade'

def registrar_historico(idade):
    registro = {
        "idade": idade, 
        "faixa": faixa_etaria(idade), 
        "maioridade": maior_idade(idade)
        }
    historico.append(registro)

def exibir_historico():
    if not historico:
        print('Ainda não há histórico.')
    else:
        for i, registro in enumerate(historico, start=1):
            print(f"{i}° registro: {registro['idade']} anos → {registro['faixa']}, {registro['maioridade']}")

def limpar_historico():
    historico.clear()
    print('Histórico limpo com sucesso.')

def main():
    while True:
        decisao_acao = menu_principal()

        if decisao_acao == 1:
            idade = validar_mensagem('Digite uma idade: ')
            print(f'Uma pessoa com {idade} é considerada: {faixa_etaria(idade)}')
            print(f'Status da maioridade brasileira: {maior_idade(idade)}')
            registrar_historico(idade)
        elif decisao_acao == 2:
            metricas()
        elif decisao_acao == 3:
            exibir_historico()
        elif decisao_acao == 4:
            limpar_historico()
        elif decisao_acao == 0:
            print('Obrigado por usar meu programa!')
            break
        else:
            continue

if __name__ == '__main__':
    main()