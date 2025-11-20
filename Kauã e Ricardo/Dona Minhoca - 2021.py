
#Importando deque e defaultdict da biblioteca collections
from collections import deque, defaultdict

def busca_largura(inicio, grafo):

    #Determina dist como uma lista que recebe valores -1 vezes o tamanho do grafo, isso segnifica que esses valores não foram visitados anteriormente
    dist = [-1] * (len(grafo))

    #Determina que no indíce do inicio terá o valor 0, pois a distancia do inicio para o inicio é zero.
    dist[inicio] = 0

    #Cria uma lista deque, a qual é mais manipulável que uma lista comum, pois será necessário a utilização de um método de gestão denominado FIFO (First-In, First-Out)
    fila = deque([inicio])

    #Enquanto tiver algum valor na fila o algoritmo continuará rodando
    while fila:

        #A função popLeft retira o primeiro número da fila e o retorna, assim a variavel atual receberá esse número
        atual = fila.popleft()

        #Aqui será feito a verificação e denominação da distancia da primeira sala para as demais
        for vizinho in grafo[atual]:
            if dist[vizinho] == -1:
                dist[vizinho] = dist[atual] + 1
                fila.append(vizinho)

    #Percorre a lista dist, ou seja, a lista que está armazenadas as distancias com base no tamanho do grafo
    mais_distante = max(range(1, len(grafo)), key=lambda sala_grafo: dist[sala_grafo])

    #Retorna a lista de distancias e um extremo
    return dist, mais_distante


def dona_minhoca():
    #Entrada de dados
    N = int(input())

    #Criação do grafo com um índice a mais do necessário, os índice irão respresentar o número de cada sala, logo como a questão pede para começar do número 1, o índice 0 nunca será utilizado, portanto à necessidade de criar um índice a mais (N+1)
    grafo = [[] for _ in range(N + 1)]

    #Colocando os valores no grafo representando onde cada sala se conecta
    for _ in range(N - 1):
        X, Y = map(int, input().split())
        grafo[X].append(Y)
        grafo[Y].append(X)

    #Primeiro vai procurar uma das salas que está na extremidade 
    _, extremoA = busca_largura(1, grafo)

    #Agora vai buscar outro extremo com base no extremoA e também a distancia do extremoA até o extremoB, determinada pela variável distA
    distA, extremoB = busca_largura(extremoA, grafo)

    #O dado diametro é determinado pela lista que é recebida em distA no índice do extremoB, ou seja, o valor da distancia entre extreminadade A e B
    diametro = distA[extremoB]

    #Busca a lista de distancia de B, ou seja, os valores da distancia entre B e as demais salas
    distB, _ = busca_largura(extremoB, grafo)

    #Formação de dicionários para contar quantas salas estão a cada distancia do ponto A e ponto B (Distancia da sala : Quantidade de Salas)
    contA = defaultdict(int)
    contB = defaultdict(int)
    for i in range(1, N + 1):
        contA[distA[i]] += 1
        contB[distB[i]] += 1

    #Verificação para encontrar quantos pares de sala tem a distancia entre eles igual ao diametro do grafo
    qtd_pares = 0
    print(contA)
    print(contB)
    for val_contA in contA:
        if (diametro - val_contA) in contB:
            qtd_pares += contA[val_contA] * contB[diametro - val_contA]

    #Saída de dados
    print(diametro + 1)
    print(qtd_pares // 2)  #Tem que ser dividido por dois para que não haja a repetição do mesmo ciclo mas com as salas inversas, por exemplo: A-B e B-A

dona_minhoca()