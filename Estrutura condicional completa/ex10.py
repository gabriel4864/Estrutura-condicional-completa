# Ler duas notas de um aluno
Nota1 = float(input("Digite a primeira nota: "))
Nota2 = float(input("Digite a segunda nota: "))
Media = (Nota1 + Nota2) / 2
print("Media: ", Media)
if Media >= 7:
    print("Aluno aprovado")
elif Media >= 5:
    print("Aluno está de exame")
else:
    print("Aluno reprovado")