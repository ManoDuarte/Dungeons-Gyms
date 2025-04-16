from carta import gerar_carta

classes_heroi = {
    "Guerreiro": {"vida": 120, "poder_extra": 5, "desc": "Combate corpo a corpo", "restricoes": ["Arco de Gelo", "Raio Divino"]},
    "Mago": {"vida": 100, "poder_extra": 10, "desc": "Mestre das magias", "restricoes": ["Espada Flamejante", "Machado Sombrio"]},
    "Arqueiro": {"vida": 110, "poder_extra": 7, "desc": "Atirador de elite", "restricoes": ["Machado Sombrio", "Raio Divino"]},
    "Paladino": {"vida": 130, "poder_extra": 3, "desc": "Defensor sagrado", "restricoes": ["Arco de Gelo", "Explosão Espiritual"]}
}

class Jogador:
    def __init__(self, nome, classe):
        c = classes_heroi[classe]
        self.nome = nome
        self.classe = classe
        self.vida_max = c["vida"]
        self.vida = self.vida_max
        self.poder_extra = c["poder_extra"]
        self.restricoes = c["restricoes"]
        self.desc = c["desc"]
        self.vivo = True
        self.cartas = [gerar_carta("ataque", self.restricoes),
                       gerar_carta("defesa", self.restricoes),
                       gerar_carta("especial", self.restricoes)]

    def mostrar_vida(self):
        barras = int((self.vida / self.vida_max) * 20)
        return f"{self.nome}: [{'█'*barras}{'.'*(20-barras)}] {self.vida}/{self.vida_max}"

    def ficha_tecnica(self):
        print(f"\n📜 FICHA DE {self.nome.upper()} ({self.classe})")
        print(f"Descrição: {self.desc}")
        print(f"Vida: {self.vida} | Poder Extra: {self.poder_extra}")
        print("Cartas:")
        for c in self.cartas:
            print(f"  - {c}")
