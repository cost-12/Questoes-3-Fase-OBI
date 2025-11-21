from math import ceil
def bolas():
    list_num = list(map(int, input().split()))
    qtd_num = [0] * 10
    num_max = ceil(len(list_num)/2)
    if 0 >= len(list_num) or len(list_num) > 8:     
        return
    else:

        #Verifica quantidade de vezes que determinado número aparece na lista
        for i in list_num:
            if not (0 <= i <= 9):
                return
            qtd_num[i] += 1

        #Verifica se tem algum número que aparece mais vezes do que o número máximo para ser possivel a organização sem vizinhos de mesmo número
        for i in qtd_num:
            if i > num_max:
                resposta = "N"
                print(resposta)
                return
    resposta = "S"    
    print(resposta)
    return
bolas()



