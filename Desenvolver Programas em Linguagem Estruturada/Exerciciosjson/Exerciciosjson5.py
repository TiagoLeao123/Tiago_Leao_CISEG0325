import json
import re

ficheiro = r"C:\Users\Tiago\Desktop\Python\Tiago_Leao_CISEG0325\Desenvolver Programas em Linguagem Estruturada\Exerciciosjson\dados.json"
dados=''

validado = []
with open(ficheiro, 'r', encoding='utf-8') as f:
    dados= json.load(f)  

email = r'[\w\.-]+@[\w\.-]+\.\w+'
nif = r'^[123568]\d{8}$'
tele = r'\d{3}[ -]?\d{3}[ -]?\d{3}'

for pessoa in dados:
    if  re.search(email, pessoa['email']) and \
        re.search(nif, pessoa['nif']) and \
        re.search(tele, pessoa['telemovel']):

        validado.append(pessoa)

print(validado)

with open(r"C:\Users\Tiago\Desktop\Python\Tiago_Leao_CISEG0325\Desenvolver Programas em Linguagem Estruturada\Exerciciosjson\dados_validos.json", 'w', encoding='utf-8') as ficheiro:
    json.dump(validado, ficheiro, indent=4)

