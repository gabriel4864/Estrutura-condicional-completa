# Perguntas sobre um crime
Contador = 0
Telefone = input("Telefonou para a vitima? (S/N): ").upper().strip()
Local = input("Esteve no local do crime? (S/N): ").upper().strip()
Residencia = input("Mora perto da vitima? (S/N): ").upper().strip()
Devia = input("Devia para a vitima? (S/N): ").upper().strip()
Trabalho = input("Ja trabalhou com a vitima? (S/N): ").upper().strip()
if Telefone == "S":
    Contador += 1
if Local == "S":
    Contador += 1
if Residencia == "S":
    Contador += 1
if Devia == "S":
    Contador += 1
if Trabalho == "S":
    Contador += 1
if Contador == 1 or Contador ==2:
    print("Suspeita")
elif Contador == 3 or Contador == 4:
    print("Cumplice")
elif Contador == 5:
    print("Assassino")
else:
    print("Inocente")