#EXERCÍCIOS 1:
#Utilize condicionais

#Acessar a Aula - 8

# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
# 2*
# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
# 3*
# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
# 4*
# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno
# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
# 5*
	# Determine se um número é múltiplo de 5 e 7.
# 6*
# Verifique se um número é positivo e maior que 10
# 7*
# Verifique se um número é divisível por 3 ou 5.




# EXERCÍCIO 1 - Positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo")

elif numero < 0:
    print("O número é negativo")

else:
    print("O número é zero")


# ----------------------------------------

# EXERCÍCIO 2 - Pode votar

idade = int(input("\nDigite sua idade: "))

if idade >= 16:
    print("Você pode votar")

else:
    print("Você ainda não pode votar")


# ----------------------------------------

# EXERCÍCIO 3 - Par ou ímpar

numero2 = int(input("\nDigite um número: "))

if numero2 % 2 == 0:
    print("O número é par")

else:
    print("O número é ímpar")


# ----------------------------------------

# EXERCÍCIO 4 - Tipo de triângulo

lado1 = float(input("\nDigite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Triângulo equilátero")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo isósceles")

else:
    print("Triângulo escaleno")


# ----------------------------------------

# EXERCÍCIO 5 - Múltiplo de 5 e 7

numero3 = int(input("\nDigite um número: "))

if numero3 % 5 == 0 and numero3 % 7 == 0:
    print("É múltiplo de 5 e 7")

else:
    print("Não é múltiplo de 5 e 7")


# ----------------------------------------

# EXERCÍCIO 6 - Positivo e maior que 10

numero4 = int(input("\nDigite um número: "))

if numero4 > 0 and numero4 > 10:
    print("É positivo e maior que 10")

else:
    print("Não é positivo e maior que 10")


# ----------------------------------------

# EXERCÍCIO 7 - Divisível por 3 ou 5

numero5 = int(input("\nDigite um número: "))

if numero5 % 3 == 0 or numero5 % 5 == 0:
    print("É divisível por 3 ou 5")

else:
    print("Não é divisível por 3 nem por 5")