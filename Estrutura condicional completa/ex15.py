# Conversão de temperatura
Conversao = input("Digite qual conversão quer fazer (C para F) ou (F para C): ").upper().strip()
if Conversao == "C PARA F":
    C = float(input("Digite a temperatura em celsius: "))
    F = C * 1.8 + 32
    print("A temperatura convertida para fahrenheit é: ", F)
else:
    F = float(input("Digite a temperatura em fahrenheit: "))
    C = (F - 32) / 1.8
    print("A temperatura convertida para celsius é: ", C)