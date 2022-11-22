'''                 legenda 

                Estados

   Posicão 0 = 3 Missionários do lado esquerdo 
   Posição 1 = 3 Canibais do lado esquerdo
   Posição 2 = 0 Missionários do lado direito 
   Posição 3 = 0 Canibais do lado direito 
   Posição 4 = Lado da canoa , Esquerda = 0 , Direito = 1

                
                Operadores 
    {1,0} - Atravesar um missionario no barnco 
    {2,0} - Atrvasares dois missionarios no barco
    {1,1} - Atravassarem um canibal e um missionário no barco
    {0,2} - Atravessarem dois canibaus no barco 
    {0,1} - atravessar um canibal no barco
    
'''   




estadoInicial = [3,3,0,0,0]
operadores = [(1,0), (1,1), (2,0), (0,2)]
borda = []
visitados = []


def deslocarCanoa(estadoAtual, numeroMissionario = 0, numeroCanibais = 0):

    if numeroCanibais + numeroMissionario > 2 :
        return
    if estadoAtual[-1] == 0 :
        
        missionarioOrigem = 0
        CanibaisOrigem = 1
        missionarioDestino = 2
        canibaisDestino = 3

    else:
        missionarioOrigem = 2
        CanibaisOrigem = 3
        missionarioDestino = 0
        canibaisDestino = 1

    if(estadoAtual[missionarioOrigem] ==  0 and estadoAtual[CanibaisOrigem] ==0):
        return

    estadoAtual[-1] = 1 - estadoAtual[-1]

    for i in range(min(numeroMissionario,estadoAtual[missionarioOrigem])):
        estadoAtual[missionarioOrigem] -=1
        estadoAtual[missionarioDestino] +=1
        
    for i in range(min(numeroCanibais,estadoAtual[CanibaisOrigem])):
        estadoAtual[CanibaisOrigem] -=1
        estadoAtual[canibaisDestino] +=1

    return estadoAtual


def sucessores(estado):
    sucessores = []

    for(i,j) in operadores:
        s = deslocarCanoa(estado[:],i,j)
        if s == None: continue
        if (s[0] < s[1] and s[0] > 0) or (s[2] < s[3] and s[2] > 0):  continue
        if s in visitados: continue
        sucessores.append(s)

    return sucessores


def obtemAdjacenteNaoVisitado(elementoAnalisar):
    l = sucessores(elementoAnalisar)

    if len(l) > 0:
        return l[0]
    else:
        return -1 

def testeMeta(estado):
    if estado[2] >= 3 and estado[3] >= 3:
        return True
    else:
        return False


def buscaEmProfundidade(estadoInicial):
    borda.append(estadoInicial)

    while len(borda) != 0:
        elementoAnalisar = borda[len(borda) -1]
        if testeMeta(elementoAnalisar) : break
        v = obtemAdjacenteNaoVisitado(elementoAnalisar)
        if v == -1 :
            borda.pop()
        else:
            visitados.append(v)
            borda.append(v)
    else:
        print("busca sem sucesso")

    return borda


def printResultado(resultados):

    for i in range(1, len(resultados)):
        missionarioDestino = abs(resultados[i][0] - resultados[i-1][0])
        canibaisDestino = abs(resultados[i][1] - resultados[i-1][1])
        canoa = resultados[i][4] - resultados[i-1][4]
        if canoa == 1:
            direcao = "Direita"
        else:
            direcao = "Esquerda"
        print(resultados[i-1],"( {} Missionário,{} Canibal  ,{})".format(missionarioDestino,canibaisDestino,direcao))




resultados = buscaEmProfundidade(estadoInicial)

printResultado(resultados)



    


