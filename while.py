numero_sorteado = 15

numero_escolhido = int(input("Escolha um número entre 1 e 20: "))

while numero_escolhido != numero_sorteado:
    print("Você errou o número, tente novamente...")

    numero_escolhido = int(input("Informe um número entre 1 e 20: "))

    print("Parabéns! Você acertou!")

    
    # Estrutura com contador ex 2
contador = 0

while contador < 10:
        print(contador)

        contador = contador + 1