import unicodedata
from collections import Counter
from typing import Dict

def remover_acentos(texto: str) -> str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def analisar_texto(texto: str) -> Dict[str, int]:
    texto = remover_acentos(texto.lower())

    vogais = 0
    consoantes = 0
    numeros = 0
    simbolos = 0

    for char in texto:
        if char.isalpha():
            if char in "aeiou":
                vogais += 1
            else:
                consoantes += 1
        elif char.isdigit():
            numeros += 1
        elif not char.isspace():
            simbolos += 1

    return {
        "caracteres": len(texto),
        "letras": vogais + consoantes,
        "vogais": vogais,
        "consoantes": consoantes,
        "numeros": numeros,
        "simbolos": simbolos,
    }

def exibir_resultados(metricas: Dict[str, int], frequencia: Counter) -> None:
    print("\n--- Resultado da Análise ---")
    print(f"Quantidade de caracteres: {metricas['caracteres']}")
    print(f"Quantidade de letras: {metricas['letras']}")
    print(f"Quantidade de vogais: {metricas['vogais']}")
    print(f"Quantidade de consoantes: {metricas['consoantes']}")
    print(f"Quantidade de números: {metricas['numeros']}")
    print(f"Quantidade de símbolos: {metricas['simbolos']}")
    print("\nFrequência de caracteres:")
    print(frequencia)

def main() -> None:
    print('--- Contador de Frases ---')
    frase = input('Digite uma frase: ')

    metricas = analisar_texto(frase)
    frequencia = Counter(remover_acentos(frase.lower()))

    exibir_resultados(metricas, frequencia)

if __name__ == "__main__":
    main()