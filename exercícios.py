#Atividades para trabalhar com try and except

#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

#Exercício 2:
#Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

#Exercício 3:
#Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número {numero}.")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
print()
print()
print()

try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    resultado = numero1 / numero2
    print(f"O resultado da divisão é {resultado}.")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
except ValueError:
    print("Erro: Digite apenas números válidos.")

print()
print()
print()

lista = ["maçã", "banana", "laranja", "uva"]

try:
    indice = int(input("Digite o índice que deseja acessar (0 a 3): "))
    print(f"O elemento no índice {indice} é {lista[indice]}.")
    
except IndexError:
    print("Erro: Índice inválido. Esse índice não existe na lista.")
except ValueError:
    print("Erro: Digite um número inteiro válido.")

