print('---Contador de Frases---')

dC = 0
dV = 0
dN = 0
dS = 0

LETRAS = CONSOANTES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
VOGAIS = ['a', 'e', 'i', 'o', 'u']
CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SIMBOLOS = ['"', "'", '!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}']

def remover_acentos(texto):
    mapa = {
        'á':'a', 'à':'a', 'ã':'a', 'â':'a', 'ä':'a',
        'é':'e', 'è':'e', 'ê':'e', 'ë':'e',
        'í':'i', 'ì':'i', 'î':'i', 'ï':'i',
        'ó':'o', 'ò':'o', 'õ':'o', 'ô':'o', 'ö':'o',
        'ú':'u', 'ù':'u', 'û':'u', 'ü':'u',
        'ç':'c',
        'Á':'A', 'À':'A', 'Ã':'A', 'Â':'A', 'Ä':'A',
        'É':'E', 'È':'E', 'Ê':'E', 'Ë':'E',
        'Í':'I', 'Ì':'I', 'Î':'I', 'Ï':'I',
        'Ó':'O', 'Ò':'O', 'Õ':'O', 'Ô':'O', 'Ö':'O',
        'Ú':'U', 'Ù':'U', 'Û':'U', 'Ü':'U',
        'Ç':'C'
    }

    resultado = ''
    for char in texto:
        resultado += mapa.get(char, char)

    return resultado

frase = list(input('Digite uma frase: ').lower())
frase = remover_acentos(frase)

frequencia = {}
for LETRAS in frase:
    if LETRAS in frequencia:
        frequencia[LETRAS] += 1
    else:
        frequencia[LETRAS] = 1

for i in range(len(frase)):
    for i2 in range(len(VOGAIS)):
        if frase[i] == VOGAIS[i2]:
            dV = dV + 1

    for i2 in range(len(CONSOANTES)):
        if frase[i] == CONSOANTES[i2]:
            dC = dC + 1

    for i2 in range(len(NUMEROS)):
        if frase[i] == NUMEROS[i2]:
            dN = dN + 1

    for i2 in range(len(SIMBOLOS)):
        if frase[i] == SIMBOLOS[i2]:
            dS = dS + 1

print(f'Quantidade de caracteres: {len(frase)}\nQuantidade de letras: {dV + dC}\nQuantidade de vogais: {dV}\nQuantidade de consoantes: {dC}')
print(f'Quantidade de números: {dN}\nQuantidade de símbolos: {dS}')
print(frequencia)