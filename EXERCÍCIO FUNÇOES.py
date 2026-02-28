#Exercícios com funções:
#variáveis locais, globais e parâmetros
#1.CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.

def verificar_par_impar(num1, num2):
    # variáveis locais
    resultado1 = "par" if num1 % 2 == 0 else "ímpar"
    resultado2 = "par" if num2 % 2 == 0 else "ímpar"
    
    print(f"O número {num1} é {resultado1}.")
    print(f"O número {num2} é {resultado2}.")


try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    verificar_par_impar(n1, n2)
except ValueError:
    print("Erro: Digite apenas números inteiros.") 
    print()
    print()
    print()


#2.CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
def multiplicar(a, b, c):
    return a * b * c


try:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    z = float(input("Digite o terceiro número: "))
    
    resultado = multiplicar(x, y, z)
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: Digite apenas números válidos.")


print()
print()
print()
#3.CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
def potencia(base, expoente):
    return base ** expoente


try:
    base = float(input("Digite um número para a base: "))
    expoente = float(input("Digite o expoente: "))
    
    print(f"Resultado: {potencia(base, expoente)}")
except ValueError:
    print("Erro: Digite números válidos.")
print()
print()
print()


#4.CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO DIGITAR, 18 ANOS.
def verificar_idade(idade):
    if idade == 18:
        print("Você tem 18 anos! Já pode tirar habilitação 🎉")
    else:
        print("Idade diferente de 18 anos.")


try:
    idade_usuario = int(input("Digite sua idade: "))
    verificar_idade(idade_usuario)
except ValueError:
    print("Erro: Digite um número válido.")
print()
print()
print()


#5.DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade


try:
    ano = int(input("Digite seu ano de nascimento: "))
    print(f"Sua idade é: {calcular_idade(ano)} anos.")
except ValueError:
    print("Erro: Digite um ano válido.")
print()
print()
print()


#6.DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
def verificar_copa(ano):
    if ano == 1999:
        print("O Brasil NÃO ganhou Copa do Mundo em 1999.")
    else:
        print("Ano diferente de 1999.")


try:
    ano = int(input("Digite o ano da Copa: "))
    verificar_copa(ano)
except ValueError:
    print("Digite um ano válido.")
print()
print()
print()


#7.DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.
#1 - Função - cumprimentar o cliente
#2 - Função - restaurante
#3 - Sugestão utilize listas e loops 
# variável global
cardapio = ["Salada", "Macarronada", "Sanduíche", "Sorvete"]


def cumprimentar():
    print("🍽️ Bem-vindo ao Restaurante Python!")
    print("Escolha uma opção do nosso cardápio:\n")


def restaurante():
    while True:
        for i, item in enumerate(cardapio):
            print(f"{i + 1} - {item}")
        
        print("0 - Sair")
        
        try:
            escolha = int(input("\nDigite o número da sua escolha: "))
            
            if escolha == 0:
                print("Obrigado pela visita! Volte sempre 😊")
                break
            elif 1 <= escolha <= len(cardapio):
                print(f"Você escolheu: {cardapio[escolha - 1]} 🍴")
            else:
                print("Opção inválida.")
                
        except ValueError:
            print("Erro: Digite apenas números.")


# Executando o sistema
cumprimentar()
restaurante()
