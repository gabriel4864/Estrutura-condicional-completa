# Placar de um jogo de futebol
Time1 = int(input("Digite a quantidade de gols do primeiro time: "))
Time2 = int(input("Digite a quantidade de gols do segundo time: "))
if Time1 > Time2:
    print("Time 1 ganhou o jogo!")
elif Time1 < Time2:
    print("Time 2 ganhou o jogo!")
else:
    print("O jogo terminou empatado!")