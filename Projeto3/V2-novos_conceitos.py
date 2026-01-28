historico = []

def pergunta():
    while True:
        try:
            temperatura = float(input('Qual a temperatura para ser convertida?: '))
        except ValueError:
            print('Você digitou algo diferente de um número ou usou "," invés de "." para separar as casas decimais.')
            continue
        return temperatura

def celsius_kelvin():
    k = round(temperatura + 273.15, 4)
    historico.append('K:')
    historico.append(k)
    return k

def celsius_fahrenheit():
    f = round((temperatura * 1.8) + 32, 4)
    historico.append('F:')
    historico.append(f)
    return f

def fahrenheit_celsius():
    c = round((temperatura - 32) * (5/9), 4)
    historico.append('C:')
    historico.append(c)
    return c

def fahrenheit_kelvin():
    k = round((temperatura - 32) * 5/9 + 273.15, 4)
    historico.append('K:')
    historico.append(k)
    return k

def kelvin_celsius():
    c = round(temperatura - 273.15, 4)
    historico.append('C:')
    historico.append(c)
    return c

def kelvin_fahrenheit():
    f = round((temperatura - 273.15) * 1.8 + 32, 4)
    historico.append('F:')
    historico.append(f)
    return f

print('----------------------------------------')
print('     Conversor de temperatura')

while True:
    print('----------------------------------------')
    print('[1] Converter de Celsius para Kelvin')
    print('[2] Converter de Celsius para Fahrenheit')
    print('[3] Converter de Fahrenheit para Celsius')
    print('[4] Converter de Fahrenheit para Kelvin')
    print('[5] Converter de Kelvin para Celsius')
    print('[6] Converter de Kelvin para Fahrenheit')
    print('[7] Ver histórico de conversões')
    print('[0] Sair')
    print('----------------------------------------')

    acao_escolhida = input('Qual conversão será feita?: ')
    if acao_escolhida.isdigit():
        acao_escolhida = int(acao_escolhida)
        if acao_escolhida == 1:
            temperatura = pergunta()
            k = celsius_kelvin()

            if k < 0:
                print('Não existe uma temperatura abaixo do 0 kelvin ou o 0 absoluto.')
                continue
            elif k > 1.41 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°C é equivalente a {k}°K')
        elif acao_escolhida == 2:
            temperatura = pergunta()
            f = celsius_fahrenheit()

            if f < -459.67:
                print('Não existe uma temperatura abaixo dos -459,67 F°, pois seria considerada abaixo do 0 absoluto')
                continue
            elif f > 2.54 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°C é equivalente a {f}°F')
        elif acao_escolhida == 3:
            temperatura = pergunta()
            c = fahrenheit_celsius()

            if c < -273.15:
                print('Não existe uma temperatura abaixo de -273.15 C°, pois seria considerada abaixo do 0 absoluto')
                continue
            elif c > 1.41 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°F é equivalente a {c}°C')
        elif acao_escolhida == 4:
            temperatura = pergunta()
            k = fahrenheit_kelvin()

            if k < 0:
                print('Não existe uma temperatura abaixo do 0 kelvin ou o 0 absoluto.')
                continue
            elif k > 1.41 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°F é equivalente a {k}°K')
        elif acao_escolhida == 5:
            temperatura = pergunta()
            c = kelvin_celsius()

            if c < -273.15:
                print('Não existe uma temperatura abaixo de -273.15 C°, pois seria considerada abaixo do 0 absoluto')
                continue
            elif c > 1.41 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°K é equivalente a {c}°C')
        elif acao_escolhida == 6:
            temperatura = pergunta()
            f = kelvin_fahrenheit()

            if f < -459.67:
                print('Não existe uma temperatura abaixo dos -459,67F° pois é considerado uma temperatura abaixo do 0 absoluto')
                continue
            elif f > 2.54 * (10 ** 32):
                print('Valor impossível')
                continue

            print(f'{temperatura}°K é equiavalente a {f}°F')
        elif acao_escolhida == 7:
            print(historico)
        elif acao_escolhida == 0:
            break
    else:
        print('Você digitou algo diferente de um número!')
        continue