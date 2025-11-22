"""Estrada
Para melhorar a integração com os países vizinhos, o Rei da Nlogônia decidiu que uma nova estrada será construída cruzando o país, da fronteira oeste à fronteira leste. O formato da estrada é uma única reta, que passará pelo centro de algumas cidades.

O Rei também decidiu que a construção será paga pelo Tesouro Real, mas cada cidade pela qual a estrada passar será responsável pela manutenção do trecho da estrada que constitui a vizinhança da estrada para aquela cidade. A vizinhança da estrada de uma cidade A é definida como todos os pontos da estrada que são mais próximos do centro da cidade A do que do centro de qualquer outra cidade.

Dados o comprimento total da estrada, de fronteira a fronteira, e as distâncias da fronteira oeste até os centros de cada cidade ao longo da nova estrada, escreva um programa para determinar qual a menor vizinhança de estrada entre as cidades pelas quais a estrada vai passar.

Entrada
A primeira linha da entrada contém um inteiro T, o comprimento total da estrada. A segunda linha contém um inteiro N, o número de cidades pelas quais a estrada vai passar. Cada uma das N linhas seguintes contém um inteiro Xi, indicando a distância da fronteira oeste até o centro da cidade i. Não há cidades nas fronteiras e cada centro de cidade tem uma localização distinta.

Saída
Seu programa deve produzir uma única linha, contendo um número real com duas casas após o ponto decimal, a menor vizinhança de estrada entre as cidades pelas quais a estrada vai passar.

Restrições
3 ≤ T ≤ 106
2 ≤ N ≤ 104
0 < Xi < T, para 1 ≤ i ≤ N
Xi ≠ X, para todo par 1 ≤ i,j ≤ N.
Informações sobre a pontuação
Para um conjunto de casos de testes valendo 10 pontos, N = 2.
Para um conjunto de casos de testes valendo 90 pontos adicionais, nenhuma outra restrição."""

# Leitura do comprimento total da estrada
T = int(input())

# Leitura do número de cidades
N = int(input())

# Leitura das posições das cidades
X = [int(input()) for _ in range(N)]

# Ordena as cidades para facilitar o cálculo das vizinhanças
X.sort()

# Lista para armazenar a vizinhança de cada cidade
viz = []

# Calcula a vizinhança de cada cidade
for i in range(N):
    if i == 0:
        # Primeira cidade: vai da fronteira oeste até o ponto médio com a próxima cidade
        v = X[0] + (X[1] - X[0]) / 2
    elif i == N - 1:
        # Última cidade: vai do ponto médio com a anterior até a fronteira leste
        v = (T - X[-1]) + (X[-1] - X[-2]) / 2
    else:
        # Cidades do meio: metade da distância entre a cidade anterior e a próxima
        v = (X[i + 1] - X[i - 1]) / 2
    viz.append(v)

# Imprime a menor vizinhança com duas casas decimais
print(f"{min(viz):.2f}")