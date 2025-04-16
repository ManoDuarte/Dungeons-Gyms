from narrador import narrar
from util import rolar_dado
from monstro import Monstro

def combate_conjunto(jogadores, rodada):
    monstro = Monstro(rodada)
    narrar(f"⚠️ Um {monstro.nome} apareceu (Nv {monstro.nivel})!")

    while monstro.vida > 0 and any(j.vivo for j in jogadores):
        print("\n== STATUS ==")
        for j in jogadores:
            print(j.mostrar_vida())
        print(monstro.mostrar_vida())

        for j in jogadores:
            if not j.vivo: continue
            print(f"\n🧝 Turno de {j.nome}")
            print("1 - Atacar | 2 - Defender | 3 - Especial | 4 - Fugir")
            try:
                acao = int(input("Escolha: "))
                if acao == 4:
                    narrar(f"{j.nome} tentou fugir... mas a porta está trancada! 😨")
                    continue
                resultado = rolar_dado()
                carta = j.cartas[acao - 1]

                if carta.tipo == "ataque":
                    dano = carta.poder + j.poder_extra if resultado > 10 else carta.poder // 2
                    monstro.vida -= dano
                    narrar(f"{j.nome} usou {carta.nome} e causou {dano}!")
                elif carta.tipo == "defesa":
                    narrar(f"{j.nome} se preparou para defender.")
                elif carta.tipo == "especial":
                    if "cura" in carta.nome.lower():
                        cura = carta.poder if resultado > 10 else carta.poder // 2
                        j.vida = min(j.vida + cura, j.vida_max)
                        narrar(f"{j.nome} recuperou {cura} de vida!")
                    else:
                        dano = carta.poder + j.poder_extra if resultado > 10 else carta.poder // 2
                        monstro.vida -= dano
                        narrar(f"{j.nome} usou {carta.nome} causando {dano}!")
            except (ValueError, IndexError):
                narrar("Escolha inválida.")

        # monstro ataca
        for j in jogadores:
            if j.vivo and monstro.vida > 0:
                j.vida -= monstro.poder
                narrar(f"{monstro.nome} atacou {j.nome} causando {monstro.poder}")
                if j.vida <= 0:
                    j.vivo = False
                    narrar(f"{j.nome} foi derrotado...")

    if monstro.vida <= 0:
        narrar("🎉 Monstro derrotado! Todos os heróis ganham +5 de poder extra!")
        for j in jogadores:
            if j.vivo:
                j.poder_extra += 5
