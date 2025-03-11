#calculadora
num=float(input("Digite um número:"))
num1=float(input("Digite mais um número:"))
operador = input("Digite um operador (+,-,*,/):")
match operador:
    case "+":
        print(num+num1)
    case "-":
        print(num-num1)
    case "*":
        print(num*num1)
    case "/":
        print(num/num1)
    case _ :
        print("Operador inválido")