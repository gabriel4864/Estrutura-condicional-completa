# Temperatura “quente”, “frio” ou “agradável”
Temperatura = float(input("Digite a temperatura: "))
if Temperatura <= 18:
    print("O clima esta frio!")
elif Temperatura < 25:
    print("O clima esta agradavel!")
else:
    print("O clima esta quente!")