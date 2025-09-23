#Exercicio 6 : Criar um ficheiro .txt com a keys nome e email

import re
import json

conteudo = r"C:\Users\Tiago\Desktop\Python\Tiago_Leao_CISEG0325\Desenvolver Programas em Linguagem Estruturada\Exerciciosjson\dados_validos.json"
conteudo2 = r"C:\Users\Tiago\Desktop\Python\Tiago_Leao_CISEG0325\Desenvolver Programas em Linguagem Estruturada\Exerciciosjson\nomesemails.txt"
with open(conteudo, 'r') as f:
    data = json.load(f)

with open(conteudo2, 'w') as f:
    for entry in data:
        nome = entry.get('nome')
        email = entry.get('email') 
        f.write(f'Nome: {nome}, Email: {email}\n')
        print(f'Nome: {nome}, Email: {email}')