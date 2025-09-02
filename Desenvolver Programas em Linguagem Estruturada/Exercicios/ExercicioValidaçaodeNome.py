'''Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.

Exemplo:

Pedro Pereira

Se o nome for válido, o programa deve exibir:
"Nome válido!"
Caso contrário, deve exibir:
"Nome inválido: contém caracteres não permitidos."

No caso de o programa encontrar um caractere invalido deve parar a execução.

Exemplos Inválidos:

Miguel PriMo

Luis AnseLmo

Guilherme ramos'''

nome=input("Introduza o seu primeiro e ultimo nome: ")

#/////////////////////////////////////////////////////////

# Validação do nome com codigos da Tabela ASCII
for char in nome: #enumerate espera um tuplo, sem as duas variaveis nao funciona
    if not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 or ord(char) == 32):  #65 = A, 90 = Z, 97 = a, 122 = z
        print("Nome inválido: contém caracteres não permitidos.")
        exit()
    if i > 0 and nome[i-1] == " " and not (65 <= ord(char) <= 90):
        print("Nome inválido: a primeira letra de cada palavra deve ser maiúscula.")
        exit()

print("Nome válido!")

# ////////////////////////////////////////////////////////

#Tabela ASCII (stackoverflow) 
for i in range(ord("A"), ord('Z')+1):
    print (f"ASCII[{i:3d}] = ´'{chr(i)}'")

#/////////////////////////////////////////////////////////

##com .isalpha ()

nome =0
listanome =[]
i =0
nome = input("Insira o seu primeiro e ultimo nome: ")

### Validar

listanome.append(nome)

while i<len(listanome):
    it=0
    while it<len(listanome[i]):
        ch = listanome[i][it]


#Verificar se é letra OU espaço

if not (ch.isalpha() or ch == " "):
    print("Nome Invalido!")

if it == 0 or listanome[i][it-1] == " ":
    if not ch.isupper():
        print("Nome Invalido") 
        exit()

print(f"{ch} -» {ord(ch)}")   

it += 1
i+= 1