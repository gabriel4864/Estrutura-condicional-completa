# Reajuste de salários
Salario = float(input("Digite o salário do funcionário: "))
if Salario <= 280:
    Aumento = Salario * 0.2
    Salario_Reajustado = (Salario * 0.2) + Salario
    print("Salário antes do reajuste: ", Salario)
    print("Percentual de aumento aplicado: 20%")
    print("Valor do aumento: ", Aumento)
    print("Novo salário: ", Salario_Reajustado)
elif Salario <= 700:
    Aumento = Salario * 0.15
    Salario_Reajustado = (Salario * 0.15) + Salario
    print("Salário antes do reajuste: ", Salario)
    print("Percentual de aumento aplicado: 15%")
    print("Valor do aumento: ", Aumento)
    print("Novo salário: ", Salario_Reajustado)
elif Salario <= 1500:
    umento = Salario * 0.10
    Salario_Reajustado = (Salario * 0.10) + Salario
    print("Salário antes do reajuste: ", Salario)
    print("Percentual de aumento aplicado: 10%")
    print("Valor do aumento: ", Aumento)
    print("Novo salário: ", Salario_Reajustado)
else:
    Aumento = Salario * 0.05
    Salario_Reajustado = (Salario * 0.05) + Salario
    print("Salário antes do reajuste: ", Salario)
    print("Percentual de aumento aplicado: 05%")
    print("Valor do aumento: ", Aumento)
    print("Novo salário: ", Salario_Reajustado)