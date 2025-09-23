import json
import os

ficheiro = r"C:\Users\Tiago\Desktop\Python\Tiago_Leao_CISEG0325\Desenvolver Programas em Linguagem Estruturada\Exerciciosjson\dados.json"
dados=''

with open(ficheiro, 'r', encoding='utf-8') as f:
    dados= json.load(f)  
    print(dados)
