# Qual produto devo comprar
Produto1 = float(input("Digite o valor do produto 1: "))
Produto2 = float(input("Digite o valor do produto 2: "))
Produto3 = float(input("Digite o valor do produto 3: "))
if Produto1 < Produto2 and Produto1 < Produto3:
    print("Deve comprar o produto 1")
elif Produto2 < Produto1 and Produto2 < Produto3:
    print("Deve comprar o produto 2")
else:
    print("Deve comprar o produto 3")