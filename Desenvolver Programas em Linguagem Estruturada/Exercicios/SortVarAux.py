listaNum = [2,4,6,3,9,2]
#index      0 1 2 3 4 5 
#lenght 6

i=0
varAux=0
FlagTroca=True

while FlagTroca:
    FlagTroca=False
    i=0
    while i < len(listaNum):
        if i<len(listaNum)-1:
            print("valor i atual",listaNum[i],"valor i seguinte", listaNum[i+1])
            if listaNum[i] > listaNum[i+1] :
                FlagTroca=True
                print(i,"index maior", i+1)
                varAux=listaNum[i]    # guarda a posicao a subscrever
                listaNum[i]=listaNum[i+1] 
                listaNum[i+1] = varAux
        i+=1
print(listaNum)