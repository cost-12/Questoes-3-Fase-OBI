#Importação da biblioteca deque para a implementação da busca em largura
from collections import deque

def buscaLargura(inicio, grafo, n):
    #Determina dist como uma lista que recebe valores -1 vezes o tamanho do grafo, isso segnifica que esses valores não foram visitados anteriormente
    dist = [-1] * (n + 1)

    #Determina que no indíce do inicio terá o valor 0, pois a distancia do inicio para o inicio é zero.
    dist[inicio] = 0

    #Cria uma lista deque, a qual é mais manipulável que uma lista comum, pois será necessário a utilização de um método de gestão denominado FIFO (First-In, First-Out)
    fila = deque([inicio])

    #Determina que a sala mais distante é inicialmente o inicio
    mais_distante = inicio

    #Enquanto houver salas na fila
    while fila:

        #Pega a sala atual da fila e a remove da fila
        atual = fila.popleft()

        #Para cada vizinho da sala atual
        for vizinho in grafo[atual]:

            #Se o vizinho ainda não foi visitado
            if dist[vizinho] == -1:
                #Determina a distancia do vizinho como a distancia da sala atual mais 1, ou seja, a sala atual é 0, o vizinho será 1
                dist[vizinho] = dist[atual] + 1

                #Adiciona o vizinho na fila para que seus vizinhos também sejam visitados futuramente
                fila.append(vizinho)

                #Verifica se a distancia do vizinho é maior que a distancia do mais distante atual, se for, o mais distante agora será o vizinho
                if dist[vizinho] > dist[mais_distante]:
                    mais_distante = vizinho

    #Retorna o nó mais distante e a lista de distancias
    return mais_distante, dist

def donaMinhoca():

    #Leitura do número de salas
    N = int(input())

    #Criação do grafo com um índice a mais do necessário, os índice irão respresentar o número de cada sala, logo como a questão pede para começar do número 1, o índice 0 nunca será utilizado, portanto à necessidade de criar um índice a mais (N+1)
    grafo = [[] for _ in range(N + 1)]

    #Colocando os valores no grafo representando onde cada sala se conecta
    for _ in range(N - 1):
        x, y = map(int, input().split())
        grafo[x].append(y)
        grafo[y].append(x)

    #Primeiro vai procurar uma das salas que está na extremidade 
    extremoA, _ = buscaLargura(1, grafo, N)

    #Agora vai buscar outro extremo com base no extremoA e também a distancia do extremoA até o extremoB, determinada pela variável distA
    extremoB, distA = buscaLargura(extremoA, grafo, N)

    #O diametro é determinado pela lista que é recebida em distA no índice do extremoB, ou seja, o valor da distancia entre extreminadade A e B
    diametro = distA[extremoB]

    #Busca a lista de distancia de B, ou seja, os valores da distancia entre B e as demais salas
    _, distB = buscaLargura(extremoB, grafo, N)

    #Contagem de quantas salas estão na extremidade A e quantas estão na extremidade B
    countA = sum(1 for i in range(1, N+1) if distA[i] == diametro)
    countB = sum(1 for i in range(1, N+1) if distB[i] == diametro)

    #Saída de dados
    print(diametro + 1)

    #Multiplica a quantidade de salas que estão na extremidade A pela quantidade de salas que estão na extremidade B, assim encontrado o número de ciclos distisntos de diâmetro máximo
    print(countA * countB)

donaMinhoca()