# Condição (obrigatória, optativa ou proibida), em relação ao ato de votar
idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Proibido")
elif idade < 18:
    print("Optativo")
elif idade < 65:
    print("Obrigatório")
else:
    print("Optativo")