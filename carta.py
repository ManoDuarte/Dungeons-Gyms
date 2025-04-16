import random

class Carta:
    def __init__(self, nome, tipo, poder):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder

    def __str__(self):
        return f"{self.nome} ({self.tipo} | poder: {self.poder})"

def gerar_carta(tipo, restricoes):
    opcoes = {
        "ataque": ["⚔️ Espada Flamejante", "🏹 Arco de Gelo", "🪓 Machado Sombrio"],
        "defesa": ["🛡️ Escudo Leve", "🪖 Armadura Pesada", "🔮 Barreira Mágica"],
        "especial": ["🍷 Poção de Cura", "⚡ Raio Divino", "💥 Explosão Espiritual"]
    }
    while True:
        c = random.choice(opcoes[tipo])
        if c not in restricoes:
            return Carta(c, tipo, random.randint(15, 30))
