quantidadeSuditos = int(input("Quantidade de súditos: "))   # Lê o total de súditos


listaDeSuditos = list(range(1, quantidadeSuditos + 1))      # Cria a lista inicial com os súditos numerados de 1 até (N)

quantidadeTurnos = int(input("Quantidade de turnos: "))      # Lê quantos turnos serão realizados


for turno_ in range(quantidadeTurnos):                       # Loop que repete uma vez para cada turno
    numero_sorteado = int(input("Número sorteado Ti: "))     # Lê quantos turnos serão realizados
    
    nova_lista = []                                         # Lista temporária que guardará os súditos que continuam

    for posicao, sudito in enumerate(listaDeSuditos, 1):    # Percorre a lista atual com posição iniciando em 1
                                                            # sudito  = número do súdito
                                                            # posicao = posição na lista
        
        if posicao % numero_sorteado != 0:                 # Se a posição NÃO for múltipla de Ti, o súdito permanece
            nova_lista.append(sudito)                      # Adiciona o súdito que não foi removido
    
    listaDeSuditos = nova_lista                            # Atualiza a lista principal somente com os remanescentes
    

print("\nConvidados:")
for convidado in listaDeSuditos[:10000]:                   # Imprime até 10.000 convidados, caso haja mais
    print(convidado)
