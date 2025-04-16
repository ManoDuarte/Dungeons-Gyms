from jogador import Jogador, classes_heroi
from combate import combate_conjunto

print("🎮 BEM-VINDO AO RPG DE CARTAS - DUNGEON CO-OP!")
jogadores = []

for i in range(4):
    print(f"\nJogador {i+1}")
    nome = input("Nome do herói: ")
    print("Escolha uma classe:")
    for cls in classes_heroi:
        print(f"- {cls}: {classes_heroi[cls]['desc']}")
    while True:
        classe = input("Classe: ").title()
        if classe in classes_heroi:
            break
        print("Classe inválida.")
    jogador = Jogador(nome, classe)
    jogador.ficha_tecnica()
    jogadores.append(jogador)
    
# Combate em várias rodadas
for rodada in range(1, 4):  # 3 lutas de monstro
    print(f"\n⚔️ RODADA {rodada}")
    combate_conjunto(jogadores, rodada)

print("\n🏆 FIM DA DUNGEON!")
for j in jogadores:
    status = "VIVO" if j.vivo else "DERROTADO"
    print(f"{j.nome} - {status} - Poder Final: {j.poder_extra}")
