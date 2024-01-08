
#for variavel in range(5):
 #   print(variavel)

#for variavel in range(1, 11):
    #print(variavel)

# contagem de 3 em 3
#for variavel in range(1, 12, 3):
#    print(variavel)

# notas

#nota1 = float(input("Informe a nota 1: "))
#ota2 = float(input("Informe a nota 2: "))
#nota3 = float(input("Informe a nota 3: ")) 
   
soma = 0

for i in range(1, 4):
    nota = float(input(f"Informe sua nota {i}: "))

    soma = soma + nota

print(soma / 3)