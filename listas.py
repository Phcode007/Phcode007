# > LISTAS

# ANTES
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Listando as variáveis
notas = [7.9, 9.7, 8.2]

#Criação das listas
lista = []
lista = list()

lista_de_listas = [10, [1, 2, 3]]


# Indexação  

lista = [26, "Paulo", 3.14, True]

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

# Slices (fatiamento)

lista = [10, 50, 30, 40, 25, 60, 5]

print(lista[0:3])
print(lista[3:6])


# Métodos de listas

lista = [1, 3, 12, 8, 2]

#append

print("Antes do comando append", lista)

lista.append(3)

print("Depois do comando append:", lista)

#insert

lista.insert(2, 10)

print("Depois do insert:", lista)

# extend

lista2 = [1, 2, 3]

lista.extend(lista2)

print("Depois do extend:", lista)

# pop

lista.pop(0)

print("Lista após o pop", lista)

#remove

lista.remove(3)

print("Depois do remove:", lista)

# count

print("Quantidade de números 2 na lista é: ", lista.count(2))

# index

print("Índice do elemento 12", lista.index(12))

#sort

lista.sort(reverse = True)

print(lista)

# Funções para listas

# len

print(len(lista))

# sum

print(sum(lista))

# max

print("Maior elemento da lista é:", max(lista))

# min

print("Menor elemento da lista é:", min(lista))
