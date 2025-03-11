#Leia dois números, faça a soma e apresente caso seja maior que 15
Num1 = int(input("Digite um numero: "))
Num2 = int(input("Digite mais um numero: "))
Soma = Num1 + Num2
match Soma > 15:
    case True:
        print("Numero maior que 15: ", Soma)
    case _:
        print("Numero menor que 15")