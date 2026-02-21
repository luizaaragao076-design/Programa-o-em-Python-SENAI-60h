# ===== SISTEMA DE NOTAS =====

## Crie um sistema de notas alunos, com as seguintes operações:
#Utilize While ou for

 #Sistema de notas de alunos**

#Visão do professor***

#- Acesso a conta com condicionais

# chances de acessar o sistema

#- Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
#- Inserir notas (se Senha correta)
#- Fazer a média

#- Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***

#- Ao finalizar o código, insira na borda do script, no última linha:

#input(’Digite enter para sair’)


senha_correta = "1234"
tentativas = 0
acesso_liberado = False

# --- Sistema de Login ---
while tentativas < 3:
    senha = input("Digite a senha do professor: ")

    if senha == senha_correta:
        print("Acesso liberado!\n")
        acesso_liberado = True
        break
    else:
        tentativas += 1
        print(f"Senha incorreta! Tentativa {tentativas}/3\n")

if not acesso_liberado:
    print("Conta bloqueada! Senha incorreta.")
else:
    alunos = {}

    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        nome = input(f"\nDigite o nome do aluno {i+1}: ")

        notas = []
        for n in range(3):
            nota = float(input(f"Digite a nota {n+1}: "))
            notas.append(nota)

        media = sum(notas) / len(notas)

        alunos[nome] = {
            "Notas": notas,
            "Média": media
        }

    print("\n===== RESULTADO FINAL =====")
    for nome, dados in alunos.items():
        print(f"\nAluno: {nome}")
        print(f"Notas: {dados['Notas']}")
        print(f"Média: {dados['Média']:.2f}")

        if dados["Média"] >= 7:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")

input('Digite enter para sair')