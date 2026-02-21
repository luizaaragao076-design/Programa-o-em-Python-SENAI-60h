#ATIVIDADE 1

#Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.

numero = 0

while numero <= 1000:
    print(numero)
    numero += 1

#Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nomes = []
contador = 0

while contador < 10:
    nome = input(f"Digite o nome da pessoa {contador + 1}: ")
    nomes.append(nome)
    contador += 1

print("\nLista de pessoas cadastradas:")
for nome in nomes:
    print(nome)