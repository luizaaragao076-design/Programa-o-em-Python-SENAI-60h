print('EXERCÍCIOS com match/ case:')

#1: Verificando se o número é par ou ímpar

numero = int(input( 'numero: '))


match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('impar') 



#2: Verificando se um número é positivo, negativo ou zero

numero = int(input("Digite um número: "))

match numero:
    case n if n > 0:
        print("Número positivo.")
    case n if n < 0:
        print("Número negativo.")
    case _:
        print("Número é zero.")


#3: Verificando se uma string é vazia ou não

texto = input("Digite algo: ")

match texto:
    case "":
        print("A string está vazia.")
    case _:
        print("A string NÃO está vazia.")


#4: Verificando se um número é maior, menor ou igual a 10

numero = int(input("Digite um número: "))

match numero:
    case n if n > 10:
        print("Maior que 10.")
    case n if n < 10:
        print("Menor que 10.")
    case _:
        print("Igual a 10.")


#5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)

idade = int(input("Digite a idade: "))

match idade:
    case i if i <= 12:
        print("Criança")
    case i if i <= 17:
        print("Adolescente")
    case i if i <= 35:
        print("Jovem")
    case i if 36 <= i <= 64:
        print("Adulto")
    case _:
        print("Idoso")