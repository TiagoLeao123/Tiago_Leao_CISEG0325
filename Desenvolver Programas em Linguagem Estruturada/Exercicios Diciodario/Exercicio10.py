'''Pede ao utilizador para introduzir uma frase. Cria um dicionário que contenha cada palavra da frase como chave e o número de vezes que ela aparece como valor.

Exemplo de entrada:
"hoje é um bom dia e hoje o sol está a brilhar"

Resultado esperado:

{'hoje': 2, 'é': 1, 'um': 1, 'bom': 1, 'dia': 1, 'e': 1, 'o': 1, 'sol': 1, 'está': 1, 'a': 1, 'brilhar': 1}'''

frase = input("Introduza uma frase: ")
palavras = frase.split()
dicionario = {}

for palavra in palavras:
    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

print(dicionario)