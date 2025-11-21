print("Este programa pede que você digite um número inteiro e, em seguida, calcula quantos divisores ele tem.")


# Lê um número digitado pelo usuário e converte para inteiro
numero = int(input("Digite o número:")) 


# Variável que vai contar quantos divisores o número tem
quantidade_de_divisores=0


# Laço de repetição que testa todos os números de 1 até o (numero)
for iten in range(1, numero +1):    # (iten) vai assumir os valores 1, 2, 3,...(numero)
    if numero % iten == 0:      # Se o resto da divisão de (numero) por (iten) for 0, significa que (iten) é divisor de (numero)
        quantidade_de_divisores += 1    # Como (iten) é divisor, aumentamos a contagem de divisores


# Exibi o resultado (quantidade total de divisores)
print("Quantidade de Divisores desse número é:",quantidade_de_divisores)

