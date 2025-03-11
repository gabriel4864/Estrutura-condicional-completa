# Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
valor = int(input("Digite um numero: "))
if valor < 0:
    print("Valor negativo")
elif valor > 0:
    print("Valor positivo")
else:
    print("Valor neutro")