# Faça um Programa que pergunte em que turno você estuda
Turno = input("Digite em qual turno você estuda (M) para matutino / (V) para vespertino / (N) para noturno: ").upper().strip()
if Turno == "M":
    print("Bom dia!")
elif Turno == "V":
    print("Boa tarde!")
elif Turno == "N":
    print("Boa noite!")
else:
    print("Valor invalido!")