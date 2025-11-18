# ==========================================
# QUESTÃO: Zero para Cancelar
# ==========================================

# 📌 Enunciado
# Seu chefe está ao telefone, nervoso. Ele quer que você compute a soma
# de uma sequência de números que ele vai falar para você ao telefone,
# para saber o total das vendas de sua viagem de negócios.

# Quando ele diz "0", isso significa cancelar o último número informado.
# Ele pode cancelar várias vezes seguidas.

# O objetivo é somar todos os números válidos após considerar os cancelamentos.

# 📌 Exemplo:
# Fala: 1, 3, 5, 4, 0, 0, 7, 0, 0, 6
# Pilha: [1, 3] → +7 → [1, 3, 7] → cancela → [1] → +6 → [1, 6]
# Resultado final = 7

# 📌 Entrada:
# - Primeira linha: N (quantidade de valores)
# - Próximas N linhas: valores Xi

# 📌 Saída:
# - Soma final dos números após os cancelamentos

# ==========================================

# A lógica é assim:

# Quando o chefe fala um número normal, você adiciona na lista.

# Quando ele fala 0, você remove o último número (se houver).

# No final, você soma tudo o que ficou na lista.

pilha = []

print('Digite números. Digite "fim" para encerrar:')

while True:
    entrada = input()

    if entrada.lower() == "fim":
        break

    x = int(entrada)

    if x == 0:
        if pilha:
            pilha.pop()
    else:
        pilha.append(x)

print("Resultado:", sum(pilha))


# pilha começa vazia

# Se x não é zero → append(x)

# Se x é zero → pop()

# No final → sum(pilha)