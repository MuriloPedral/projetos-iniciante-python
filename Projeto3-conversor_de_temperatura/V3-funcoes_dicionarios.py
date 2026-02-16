MENU_PRINCIPAL = {
    1:  'Converter de Celsius para Kelvin',
    2:  'Converter de Celsius para Fahrenheit',
    3:  'Converter de Fahrenheit para Celsius',
    4:  'Converter de Fahrenheit para Kelvin',
    5:  'Converter de Kelvin para Celsius',
    6:  'Converter de Kelvin para Fahrenheit',
    7:  'Ver histórico de conversões',
    8:  'Apagar histórico de conversões',
    0:  'Sair'
}

historico = []

def registrar_historico(temperatura, resultado, tsi, tsc):
    registro = {
        'Temperatura_inicial': temperatura,
        'Temperatura_convertida': resultado,
        'Temperatura_sigla_inicial': tsi,
        'Temperatura_sigla_convertida': tsc
    }
    historico.append(registro)

def exibir_historico():
    if not historico:
        print('Ainda não há histórico')
    else:
        for i, registro in enumerate(historico, start=1):
            print(
                f"A {i}° conversão, transformando "
                f"{registro['Temperatura_inicial']} {registro['Temperatura_sigla_inicial']} "
                f"em → {round(registro['Temperatura_convertida'], 2)} "
                f"{registro['Temperatura_sigla_convertida']}."
            )

def apagar_historico():
    historico.clear()
    print('Histórico limpo com sucesso.')

def menu_principal():
    print('----------------------------------------')
    print('     Conversor de temperatura')
    print('----------------------------------------')

    for codigo, descricao in MENU_PRINCIPAL.items():
        print(f'[{codigo}] {descricao}')

    print('----------------------------------------')

def validar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digitou algo diferente do esperado!')

def validar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print('Digitou algo diferente do esperado!')

def sigla_temperatura(acao_escolhida):
    if acao_escolhida == 1:
        return 'C°', 'K°'
    elif acao_escolhida == 2:
        return 'C°', 'F°'
    elif acao_escolhida == 3:
        return 'F°', 'C°'
    elif acao_escolhida == 4:
        return 'F°', 'K°'
    elif acao_escolhida == 5:
        return 'K°', 'C°'
    elif acao_escolhida == 6:
        return 'K°', 'F°'

def pergunta_padrao(tsi, tsc):
    return validar_float(f'Digite a temperatura para converter {tsi} em {tsc}: ')

def celsius_kelvin(c):
    return c + 273.15

def celsius_fahrenheit(c):
    return (c * 1.8) + 32

def fahrenheit_celsius(f):
    return (f - 32) * (5 / 9)

def fahrenheit_kelvin(f):
    return (f - 32) * (5 / 9) + 273.15

def kelvin_celsius(k):
    return k - 273.15

def kelvin_fahrenheit(k):
    return (k - 273.15) * 1.8 + 32

def validar_temperatura_fisica(kelvin):
    if kelvin < 0:
        return False, 'Temperatura abaixo do zero absoluto (0 K)'
    return True, None

def exibir_resultado(resultado):
    return round(resultado, 2)

def main():
    while True:
        menu_principal()
        acao_escolhida = validar_int('Digite um número para determinar a próxima ação: ')

        if acao_escolhida == 1:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            resultado = celsius_kelvin(temperatura)
            valido, erro = validar_temperatura_fisica(resultado)

            if not valido:
                print(f'Erro: {erro}')
            else:
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 2:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            kelvin = celsius_kelvin(temperatura)
            valido, erro = validar_temperatura_fisica(kelvin)

            if not valido:
                print(f'Erro: {erro}')
            else:
                resultado = celsius_fahrenheit(temperatura)
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 3:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            kelvin = fahrenheit_kelvin(temperatura)
            valido, erro = validar_temperatura_fisica(kelvin)

            if not valido:
                print(f'Erro: {erro}')
            else:
                resultado = fahrenheit_celsius(temperatura)
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 4:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            resultado = fahrenheit_kelvin(temperatura)
            valido, erro = validar_temperatura_fisica(resultado)

            if not valido:
                print(f'Erro: {erro}')
            else:
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 5:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            valido, erro = validar_temperatura_fisica(temperatura)

            if not valido:
                print(f'Erro: {erro}')
            else:
                resultado = kelvin_celsius(temperatura)
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 6:
            tsi, tsc = sigla_temperatura(acao_escolhida)
            temperatura = pergunta_padrao(tsi, tsc)

            valido, erro = validar_temperatura_fisica(temperatura)

            if not valido:
                print(f'Erro: {erro}')
            else:
                resultado = kelvin_fahrenheit(temperatura)
                registrar_historico(temperatura, resultado, tsi, tsc)
                print(exibir_resultado(resultado))

        elif acao_escolhida == 7:
            exibir_historico()

        elif acao_escolhida == 8:
            apagar_historico()

        elif acao_escolhida == 0:
            print('Obrigado por usar meu programa!')
            break

if __name__ == '__main__':
    main()