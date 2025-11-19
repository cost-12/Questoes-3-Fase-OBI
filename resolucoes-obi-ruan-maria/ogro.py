# ==========================================
# QUESTÃO: Ogro
# ==========================================

# O Ogro da Nlogônia está aprendendo a contar até dez usando os dedos das mãos
# (assim como os humanos, ele possui 2 mãos com 5 dedos cada).
#
# Ele está treinando muito e quer um aplicativo que o ajude.
#
# A representação funciona assim:
#
# 1) Se o número puder ser mostrado usando apenas UMA mão:
#       → Mão esquerda mostra os dedos com 'I'
#       → Mão direita fica fechada, representada por '*'
#
# 2) Se o número for MAIOR que 5:
#       → Mão esquerda mostra SEMPRE os 5 dedos: "IIIII"
#       → Mão direita mostra o restante: (N - 5) dedos com 'I'
#
# 📌 Exemplos:
#    Número 3 -> esquerda: "III"     direita: "*"
#    Número 8 -> esquerda: "IIIII"   direita: "III"
#
# Entrada:
#   Um único inteiro N (0 ≤ N ≤ 10)
#
# Saída:
#   Duas linhas:
#       - Primeira linha: mão esquerda (I's ou *)
#       - Segunda linha: mão direita (I's ou *)
#
# ==========================================

# Sua tarefa é ajudar o Ogro em seu treinamento, escrevendo um programa para, dado um número entre 0 e 10, mostrar a configuração de dedos correspondente a esse número, de acordo com as regras acima.

# Mensagem inicial e um 'INPUT' que Pede ao usuário para digitar um número entre 0 e 10
print("___Ajudando o Ogro a aprender a contar usando os dedos___")

# Loop até o Ogro digitar um valor válido
while True:
    Num = int(input("Ogro: Me diga um número entre 0 e 10: \n"))
    
    if 0 <= Num <= 10:
        break  # número válido → sai do while
    else:
        print("Valor inválido! Digite apenas números entre 0 e 10.\n")

# Caso o número informado for 0 as duas maos ficam fechadas mostrando ' * *'.
if Num == 0:
    esquerda = "*"
    direita = "*"

# Nessa condição, se o número estiver entre 1 e 5 usamos somente a mão esquerda.
elif Num <= 5:
    esquerda = "I" * Num
    direita = "*"

# Mas caso o número for entre 6 e 10, a mão esquerda fica com os (5) dedos e a mão direita para completar o que falta.
else:
    esquerda = "IIIII"
    direita = "I" * (Num - 5)

# Exibe o resultado final para o usuário.
print("Mão Esquerda:", esquerda)
print("Mão Direita :", direita)

