print("Sistema de notas")
print("...."*8)

nome_aluno = input("Nome do aluno: ")
n1_port = float(input("Nota português: "))
n2_mat = float(input("Nota matemática: "))
n3_ing = float(input("Nota inglês: "))
print()
media = (n1_port+n2_mat+n3_ing)/3

print("Situação do aluno: ")
print("...."*8)
aprovado = media >= 7
reprovado = media < 5
recuperação = media >=5 and media <7
print()
print("Aprovado? - ",aprovado)
print("Reprovado? - ",reprovado)
print("Recuperação? - ",recuperação)

