nota1 = float(input(" Digite a nota1: "))
nota2 = float(input(" Digite a nota2: "))
nota3 = float(input(" Digite a nota3: "))

média = (nota1 + nota2 + nota3) / 3
print("A média do aluno é = " + str(média))

if (média >= 7):
    print(f"O Aluno foi APROVADO!!! Parabéns Com a média de: " + (média))
    if(média > 5):
        print(f"O Aluno está de RECUPERAÇÃO!!! Prescisa Melhora {média}")
else:
    print("O Aluno está REPROVADO!!! Muito burro, ficou com a média de: " + str(média))