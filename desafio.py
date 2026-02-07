# Lista de preços
precos = [100, 150, 250]  # Simples, Duplo, Luxo

# Lista dos tipos de quarto
quartos = ["Simples", "Duplo", "Luxo"]

# ---------------- CLIENTE 1 ----------------

nome1 = input("Digite o nome do Cliente 1: ")
idade1 = int(input("Digite a idade do Cliente 1: "))

print("\nTipos de quarto:")
print("1 - Simples (R$100)")
print("2 - Duplo (R$150)")
print("3 - Luxo (R$250)")

escolha1 = int(input("Escolha o quarto (1/2/3): "))
dias1 = int(input("Quantos dias vai ficar? "))

if escolha1 == 1:
    preco1 = precos[0]
elif escolha1 == 2:
    preco1 = precos[1]
else:
    preco1 = precos[2]

total1 = preco1 * dias1


# ---------------- CLIENTE 2 ----------------

nome2 = input("\nDigite o nome do Cliente 2: ")
idade2 = int(input("Digite a idade do Cliente 2: "))

print("\nTipos de quarto:")
print("1 - Simples (R$100)")
print("2 - Duplo (R$150)")
print("3 - Luxo (R$250)")

escolha2 = int(input("Escolha o quarto (1/2/3): "))
dias2 = int(input("Quantos dias vai ficar? "))

if escolha2 == 1:
    preco2 = precos[0]
elif escolha2 == 2:
    preco2 = precos[1]
else:
    preco2 = precos[2]

total2 = preco2 * dias2


# ---------------- CLIENTE 3 ----------------

nome3 = input("\nDigite o nome do Cliente 3: ")
idade3 = int(input("Digite a idade do Cliente 3: "))

print("\nTipos de quarto:")
print("1 - Simples (R$100)")
print("2 - Duplo (R$150)")
print("3 - Luxo (R$250)")

escolha3 = int(input("Escolha o quarto (1/2/3): "))
dias3 = int(input("Quantos dias vai ficar? "))

if escolha3 == 1:
    preco3 = precos[0]
elif escolha3 == 2:
    preco3 = precos[1]
else:
    preco3 = precos[2]

total3 = preco3 * dias3


# ---------------- RESULTADOS ----------------

print("\n===== RESUMO DAS RESERVAS =====")

print(f"{nome1} - Valor a pagar: R$ {total1}")
print(f"{nome2} - Valor a pagar: R$ {total2}")
print(f"{nome3} - Valor a pagar: R$ {total3}")