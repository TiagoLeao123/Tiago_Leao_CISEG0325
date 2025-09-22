alunos = {}
opcao = 0

while True:
    print("1-Inserir")
    print("2-Listar")
    opcao = int(input("Insira um opcao: "))

    if opcao == 1 :
        nome = input("Insira o seu nome: ")
        idade = input("Insira a sua idade: ")
        curso = input("Insira o seu curso: ")

        alunos[nome] = {"idade": idade, "curso": curso}     

    elif opcao == 2:
        for nome, val in alunos.items():
          print(nome)
          print(val["idade"])
          print(val["curso"])