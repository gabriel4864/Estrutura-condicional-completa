# identificando o dia da semana
# receba o número e verifique qual dia da semana ex: 1 ("Domingo")
num= int(input("Digite um número de 1 a 7:"))
match num:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido, digite um número entre 1 e 7")