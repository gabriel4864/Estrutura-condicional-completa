# Três lados de um triângulo
# Equilátero (todos os lados iguais)
# Isósceles (dois lados iguais)
#Escaleno (todos os lados diferentes)
tri= int(input("Digite o lado do primeiro triângulo:"))
tri1= int(input("Digite o lados do segundo triângulo:"))
tri2= int(input("Digite o lados do terceiro triângulo:"))
# comparação se as comparações são true
match (tri == tri1, tri1 == tri2, tri2==tri):
    case (True,True,True):
        print("O triangulo é Equilátero")
    case (True,False,False) |(False, True,False)|(False,False,True):
        print("O triangulo é Isósceles")
    case (False,False,False):
        print("Triangulo Escaleno")