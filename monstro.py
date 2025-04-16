import random

class Monstro:
    def __init__(self, rodada):
        nomes = ["👺 Goblin", "💀 Esqueleto", "🐉 Dragão", "👹 Orc", "🔥 Demônio"]
        self.nome = random.choice(nomes)
        self.nivel = random.randint(1, 2 + rodada//2)
        self.vida_max = self.nivel * 40
        self.vida = self.vida_max
        self.poder = self.nivel * 10

    def mostrar_vida(self):
        barras = int((self.vida / self.vida_max) * 20)
        return f"{self.nome} (Nv {self.nivel}): [{'█'*barras}{'.'*(20-barras)}] {self.vida}/{self.vida_max}"
